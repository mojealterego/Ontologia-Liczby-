"""Independent exact checks of F28.2-D value and residual certificates."""
import itertools
import unittest
from fractions import Fraction as Q
from test_f282d_proximal import objective, optimum, step, norm2


class TestF282DCertificates(unittest.TestCase):
    def test_t8_quadratic_case_lambda_zero(self):
        a = (Q(1), Q(3))
        lam = (Q(0), Q(0))
        y = (Q(0), Q(0))
        t = Q(1, 2)
        rho = Q(1, 2)
        for x in itertools.product([Q(-3), Q(-1), Q(0), Q(1), Q(3)], repeat=2):
            tx = step(x, a, lam, y, t)
            r2 = norm2(tuple(xi - ti for xi, ti in zip(x, tx)))
            gap = objective(x, a, lam, y) - objective(optimum(a, lam, y), a, lam, y)
            self.assertLessEqual(gap, max(a) * r2 / (2 * (1 - rho)**2))

    def test_t8_rational_upper_bound_general_lambda(self):
        a = (Q(1), Q(3))
        lam = (Q(1), Q(2))
        y = (Q(3), Q(-2))
        t = Q(1, 2)
        rho = Q(1, 2)
        for x in itertools.product([Q(-2), Q(0), Q(1), Q(4)], repeat=2):
            tx = step(x, a, lam, y, t)
            # L1 residual upper-bounds the Euclidean residual, so Ebar >= E.
            ebar = sum(abs(xi - ti) for xi, ti in zip(x, tx)) / (1 - rho)
            gap = objective(x, a, lam, y) - objective(optimum(a, lam, y), a, lam, y)
            upper = max(a) * ebar**2 / 2 + 2 * sum(lam) * ebar
            self.assertLessEqual(gap, upper)

    def test_t10_exact_gap_on_sign_branch(self):
        a = (Q(2), Q(3))
        lam = (Q(1), Q(2))
        y = (Q(3), Q(-4))
        xstar = optimum(a, lam, y)
        self.assertEqual(xstar, (Q(5, 2), Q(-10, 3)))
        for x in [(Q(1), Q(-1)), (Q(4), Q(-2)), (Q(3), Q(-4))]:
            gap = objective(x, a, lam, y) - objective(xstar, a, lam, y)
            exact = sum(ai * (xi - si)**2 / 2 for ai, xi, si in zip(a, x, xstar))
            self.assertEqual(gap, exact)

    def test_k5_small_residual_large_error(self):
        a, lam, y = (Q(1, 1000),), (Q(0),), (Q(0),)
        x = (Q(1),)
        tx = step(x, a, lam, y, Q(1))
        self.assertEqual(abs(x[0] - tx[0]), Q(1, 1000))
        self.assertEqual(abs(x[0] - optimum(a, lam, y)[0]), Q(1))

    def test_zero_contraction_one_step(self):
        a, lam, y = (Q(2), Q(2)), (Q(1), Q(3)), (Q(2), Q(-4))
        target = optimum(a, lam, y)
        for x in itertools.product([Q(-100), Q(0), Q(100)], repeat=2):
            self.assertEqual(step(x, a, lam, y, Q(1, 2)), target)


if __name__ == '__main__':
    unittest.main()
