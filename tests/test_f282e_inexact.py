"""Exact-rational regression checks for Tom I, F28.2-E.

Finite test cases support but do not formally prove the mathematical theorems.
"""
import itertools
import unittest
from fractions import Fraction as Q


def soft(v, threshold):
    assert threshold >= 0
    return max(v - threshold, Q(0)) if v >= 0 else min(v + threshold, Q(0))


def step(x, a, lam, y, t):
    assert len(x) == len(a) == len(lam) == len(y)
    assert all(ai > 0 and li >= 0 for ai, li in zip(a, lam))
    return tuple(soft((1 - t * ai) * xi + t * ai * yi, t * li)
                 for xi, ai, li, yi in zip(x, a, lam, y))


def optimum(a, lam, y):
    return tuple(soft(yi, li / ai) for ai, li, yi in zip(a, lam, y))


def squared_norm(x):
    return sum((v*v for v in x), Q(0))


def objective(x, a, lam, y):
    return sum((ai * (xi - yi)**2 / 2 + li * abs(xi)
                for xi, ai, li, yi in zip(x, a, lam, y)), Q(0))


class InexactIterationTests(unittest.TestCase):
    def test_t1_t2_unrolled_error_1d(self):
        rho, d0 = Q(1, 2), Q(4)
        errors = [Q(1, 4), Q(-1, 8), Q(1, 16), Q(-1, 32)]
        x = d0
        for k, e in enumerate(errors, start=1):
            x = rho*x + e
            upper = rho**k * d0 + sum((rho**(k-1-j) * abs(ej)
                                      for j, ej in enumerate(errors[:k])), Q(0))
            self.assertLessEqual(abs(x), upper)

    def test_t3_uniform_error_floor(self):
        rho, delta = Q(1, 2), Q(1, 4)
        x, d0 = Q(4), Q(4)
        for n in range(1, 25):
            x = rho*x + delta
            bound = rho**n*d0 + delta*(1-rho**n)/(1-rho)
            self.assertEqual(x, bound)
        self.assertEqual(delta/(1-rho), Q(1, 2))

    def test_t4_vanishing_errors_finite_witness(self):
        x = Q(0)
        for k in range(1, 101):
            x = Q(1, 2)*x + Q(1, k)
        self.assertLess(x, Q(1, 20))

    def test_t5_inexact_residual_1d(self):
        rho = Q(1, 3)
        for x, e in itertools.product([Q(-3), Q(-1), Q(0), Q(1), Q(3)],
                                       [Q(-1, 5), Q(0), Q(1, 5)]):
            z = rho*x + e
            E = (abs(x-z) + abs(e))/(1-rho)
            self.assertLessEqual(abs(x), E)

    def test_t6_two_sided_residual(self):
        rho = Q(2, 5)
        for x in [Q(-5), Q(-1, 3), Q(0), Q(7, 3)]:
            residual = abs(x-rho*x)
            self.assertLessEqual((1-rho)*abs(x), residual)
            self.assertLessEqual(residual, (1+rho)*abs(x))

    def test_t7_input_output_perturbations_2d(self):
        a, lam, y, t = (Q(1), Q(3)), (Q(1), Q(0)), (Q(3), Q(2)), Q(1, 2)
        rho = Q(1, 2)
        for x in itertools.product([Q(-2), Q(0), Q(2)], repeat=2):
            u, v = (Q(1, 10), Q(-1, 10)), (Q(1, 20), Q(0))
            actual = tuple(p+q for p,q in zip(step(tuple(p+q for p,q in zip(x,u)),a,lam,y,t),v))
            exact = step(x,a,lam,y,t)
            diff = tuple(p-q for p,q in zip(actual,exact))
            # Euclidean triangle bound, checked without floating point.
            from math import isqrt
            eta_upper = Q(1, 5)  # >= sqrt(2)/10
            xi_upper = Q(1, 20)
            self.assertLessEqual(squared_norm(diff), (rho*eta_upper+xi_upper)**2)

    def test_t8_sharp_fixed_disturbance(self):
        for rho in [Q(0), Q(1, 3), Q(1, 2), Q(9, 10)]:
            e = Q(3, 8)
            x_e = e/(1-rho)
            self.assertEqual(rho*x_e+e, x_e)
            self.assertEqual(abs(x_e), abs(e)/(1-rho))

    def test_t9_objective_bound_from_inexact_residual(self):
        a, lam, y, t = (Q(1),), (Q(1),), (Q(0),), Q(1, 2)
        rho = Q(1, 2)
        xstar = optimum(a,lam,y)
        for x,e in itertools.product([Q(-2),Q(-1),Q(0),Q(1),Q(2)], [Q(-1,10),Q(0),Q(1,10)]):
            z = step((x,),a,lam,y,t)[0]+e
            E = (abs(x-z)+abs(e))/(1-rho)
            gap = objective((x,),a,lam,y)-objective(xstar,a,lam,y)
            self.assertLessEqual(gap, max(a)*E*E/2+2*sum(lam)*E)

    def test_t10_stop_condition(self):
        rho, eps, delta = Q(1, 2), Q(1, 10), Q(1, 100)
        self.assertEqual((1-rho)*eps-delta,Q(1,25))
        self.assertEqual((Q(1,25)+delta)/(1-rho),eps)

    def test_counterexample_k1_constant_error(self):
        x=Q(0)
        for _ in range(20): x=x/2+Q(1,2)
        self.assertGreater(x,Q(99,100))
        self.assertLess(x,Q(1))

    def test_counterexample_k2_non_geometric(self):
        self.assertEqual(Q(1,101),Q(1,101))
        self.assertGreater(Q(1,101),Q(1,2)**100)

    def test_counterexample_k3_observed_zero(self):
        x,z,e=Q(1),Q(1),Q(1)
        self.assertEqual(abs(x-z),0)
        self.assertEqual(abs(x),1)
        self.assertEqual(abs(z-0),abs(e))

    def test_counterexample_k4_unstable_step(self):
        x=Q(1)
        for _ in range(10): x=-x
        self.assertEqual(x,Q(1))

    def test_counterexample_k5_small_residual(self):
        x,rho=Q(1),Q(999,1000)
        self.assertEqual(abs(x-rho*x),Q(1,1000))
        self.assertEqual(abs(x),Q(1))

    def test_counterexample_k6_nonsmooth_gap(self):
        h=Q(1,100)
        self.assertEqual(h*h/2+abs(h),Q(201,20000))
        self.assertGreater((h*h/2+abs(h))/h**2, Q(100))

    def test_z1_z3_z8(self):
        self.assertEqual(Q(1,2)**2*4+Q(1,2)*Q(1,4)+Q(1,4),Q(11,8))
        self.assertEqual((Q(1,6)+Q(1,18))/(1-Q(1,3)),Q(1,3))
        self.assertEqual(Q(2)/2*Q(1,4)**2+2*Q(1)*Q(1,4),Q(9,16))

    def test_z11_inconsistent_oracle_budget(self):
        x,z,delta=Q(2),Q(5,2),Q(1,2)
        self.assertGreater(abs(z),delta)  # T(x)=0, so oracle promise fails

    def test_z12_tight_bound(self):
        x,z,delta=Q(2),Q(1,2),Q(1,2)
        self.assertEqual(abs(x-z)+delta,abs(x))


if __name__ == '__main__':
    unittest.main()
