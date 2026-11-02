"""Deterministic exact-arithmetic checks for F28.2-D. Run: python -m unittest -v test_f282d_proximal.py"""
import itertools
import unittest
from fractions import Fraction as Q


def soft(v: Q, tau: Q) -> Q:
    assert tau >= 0
    return max(v - tau, Q(0)) if v >= 0 else min(v + tau, Q(0))


def optimum(a, lam, y):
    return tuple(soft(yi, li / ai) for ai, li, yi in zip(a, lam, y))


def step(x, a, lam, y, t):
    return tuple(soft((1 - t * ai) * xi + t * ai * yi, t * li)
                 for xi, ai, li, yi in zip(x, a, lam, y))


def norm2(v):
    return sum((z * z for z in v), Q(0))


def objective(x, a, lam, y):
    return sum((ai * (xi - yi)**2 / 2 + li * abs(xi)
                for xi, ai, li, yi in zip(x, a, lam, y)), Q(0))


class TestF282D(unittest.TestCase):
    def setUp(self):
        self.a = (Q(1), Q(3))
        self.lam = (Q(1), Q(0))
        self.y = (Q(3), Q(2))
        self.t = Q(1, 2)

    def test_soft_nonexpansive_exhaustive(self):
        vals = [Q(i, 4) for i in range(-12, 13)]
        for tau in [Q(0), Q(1, 2), Q(3)]:
            for v, w in itertools.product(vals, repeat=2):
                self.assertLessEqual(abs(soft(v, tau) - soft(w, tau)), abs(v - w))

    def test_optimum_and_fixed_point(self):
        self.assertEqual(optimum(self.a, self.lam, self.y), (Q(2), Q(2)))
        for a, lam, y in itertools.product([Q(1), Q(2)], [Q(0), Q(1)], [Q(-3), Q(0), Q(3)]):
            xstar = optimum((a,), (lam,), (y,))
            for t in [Q(1, 5), Q(1, 2), Q(1), Q(3)]:
                self.assertEqual(step(xstar, (a,), (lam,), (y,), t), xstar)

    def test_contraction_and_linear_rate(self):
        a, lam, y, t = self.a, self.lam, self.y, self.t
        rho = max(abs(1 - t * ai) for ai in a)
        self.assertEqual(rho, Q(1, 2))
        xstar = optimum(a, lam, y)
        x = (Q(0), Q(0))
        base = norm2(tuple(xi - si for xi, si in zip(x, xstar)))
        for k in range(9):
            self.assertLessEqual(norm2(tuple(xi - si for xi, si in zip(x, xstar))), rho**(2*k) * base)
            x = step(x, a, lam, y, t)

    def test_residual_a_posteriori(self):
        a, lam, y, t = self.a, self.lam, self.y, self.t
        rho = Q(1, 2)
        xstar = optimum(a, lam, y)
        for x in itertools.product([Q(-2), Q(0), Q(1), Q(4)], repeat=2):
            tx = step(x, a, lam, y, t)
            residual2 = norm2(tuple(xi - zi for xi, zi in zip(x, tx)))
            error2 = norm2(tuple(xi - si for xi, si in zip(x, xstar)))
            self.assertLessEqual(error2 * (1-rho)**2, residual2)

    def test_gap_bounds_exact(self):
        a, lam, y = self.a, self.lam, self.y
        xstar = optimum(a, lam, y)
        for x in itertools.product([Q(-3), Q(0), Q(1, 2), Q(2), Q(4)], repeat=2):
            e = tuple(xi-si for xi,si in zip(x,xstar))
            gap = objective(x,a,lam,y) - objective(xstar,a,lam,y)
            self.assertLessEqual(min(a)*norm2(e)/2, gap)
            self.assertLessEqual(gap, max(a)*norm2(e)/2 + 2*sum(li*abs(ei) for li,ei in zip(lam,e)))

    def test_optimal_step_factor(self):
        for a in [(Q(1), Q(3)), (Q(2), Q(2)), (Q(1), Q(7))]:
            amin, amax = min(a), max(a)
            t = 2/(amin+amax)
            rho = max(abs(1-t*ai) for ai in a)
            self.assertEqual(rho, (amax-amin)/(amax+amin))
            for other in [Q(1, 100), Q(1, 10), Q(1, 4), Q(1, 2), Q(1), Q(3, 2), Q(2)]:
                self.assertLessEqual(rho, max(abs(1-other*ai) for ai in a))

    def test_counterexamples(self):
        a, lam, y = (Q(1),), (Q(0),), (Q(0),)
        self.assertEqual(step((Q(1),), a, lam, y, Q(2)), (Q(-1),))
        self.assertEqual(step((Q(1),), a, lam, y, Q(3)), (Q(-2),))
        self.assertEqual(objective((Q(1,10),), a, (Q(1),), y), Q(21,200))

    def test_examples(self):
        self.assertEqual(step((Q(0),Q(0)), self.a, self.lam, self.y, self.t), (Q(1),Q(3)))
        self.assertEqual(optimum((Q(2),Q(2)),(Q(1),Q(3)),(Q(2),Q(-4))), (Q(3,2),Q(-5,2)))
        self.assertEqual(objective((Q(3),),(Q(2),),(Q(1),),(Q(3),)) -
                         objective((Q(5,2),),(Q(2),),(Q(1),),(Q(3),)), Q(1,4))

    def test_stop_threshold(self):
        a, lam, y, t = self.a, self.lam, self.y, self.t
        xstar = optimum(a, lam, y)
        rho = Q(1,2)
        for x in itertools.product([Q(-2),Q(0),Q(2),Q(3)], repeat=2):
            residual2 = norm2(tuple(u-v for u,v in zip(x,step(x,a,lam,y,t))))
            eps = Q(10)
            if residual2 <= (1-rho)**2 * eps**2:
                self.assertLessEqual(norm2(tuple(u-v for u,v in zip(x,xstar))),eps**2)


if __name__ == '__main__':
    unittest.main()
