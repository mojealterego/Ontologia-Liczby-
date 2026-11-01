"""F28.2: exact finite-instance checks of global-optimality certificates.

Tests support, but do not mechanically prove, the quantified mathematical results.
"""
from fractions import Fraction as F
import unittest


def project(x, lo, hi):
    if lo > hi:
        raise ValueError("empty interval")
    return min(hi, max(lo, x))


def quadratic(a, r, k, x):
    return a * (x-r)**2 + k


def derivative(a, r, x):
    return 2*a*(x-r)


def quadratic_lower_bound(f_c, g_c, m, c, lo, hi):
    if m <= 0 or lo > hi or not (lo <= c <= hi):
        raise ValueError("invalid certificate")
    z = project(c - g_c/m, lo, hi)
    return f_c + g_c*(z-c) + m*(z-c)**2/2


def derivative_localization(gl, gu, m, M, lo, hi):
    if not (0 < m <= M and lo <= hi and gl <= 0 <= gu):
        raise ValueError("invalid derivative bracket")
    return (max(lo, lo-gl/M, hi-gu/m),
            min(hi, lo-gl/m, hi-gu/M))


def bisect_derivative(g, lo, hi, steps):
    if steps < 0 or g(lo) > 0 or g(hi) < 0:
        raise ValueError("invalid bracket")
    for _ in range(steps):
        mid = (lo+hi)/2
        v = g(mid)
        if v == 0:
            return mid, mid
        if v < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def projected_residual(x, grad, eta, lo, hi):
    if eta <= 0:
        raise ValueError("eta must be positive")
    return (x-project(x-eta*grad, lo, hi))/eta


def can_prune(lower, incumbent_upper):
    return lower > incumbent_upper


class F282Certificates(unittest.TestCase):
    def test_projection_inside(self):
        self.assertEqual(project(F(1, 2), F(0), F(1)), F(1, 2))

    def test_projection_left(self):
        self.assertEqual(project(F(-1), F(0), F(1)), F(0))

    def test_projection_right(self):
        self.assertEqual(project(F(3), F(0), F(1)), F(1))

    def test_projection_invalid(self):
        with self.assertRaises(ValueError): project(0, 2, 1)

    def test_strong_convexity_exact_quadratic(self):
        for a in range(1, 6):
            for r in range(-3, 4):
                for x in range(-3, 4):
                    for y in range(-3, 4):
                        f_x = quadratic(F(a), F(r), F(5), F(x))
                        f_y = quadratic(F(a), F(r), F(5), F(y))
                        lower = f_x + derivative(F(a), F(r), F(x))*(y-x) + F(2*a, 2)*(y-x)**2
                        self.assertEqual(f_y, lower)

    def test_weak_lower_curvature(self):
        for x in range(-3, 4):
            for y in range(-3, 4):
                f = lambda t: t**4+t*t
                g = lambda t: 4*t**3+2*t
                self.assertGreaterEqual(f(y), f(x)+g(x)*(y-x)+(y-x)**2)

    def test_unique_quadratic_minimum(self):
        for a in range(1, 6):
            for r in range(-2, 3):
                k = F(3)
                self.assertEqual(quadratic(F(a), F(r), k, F(r)), k)
                for x in range(-4, 5):
                    if x != r:
                        self.assertGreater(quadratic(F(a), F(r), k, F(x)), k)

    def test_boundary_minimizer_with_positive_gradient(self):
        self.assertEqual(projected_residual(F(0), F(1), F(1, 4), F(0), F(1)), 0)

    def test_boundary_minimizer_with_negative_gradient(self):
        self.assertEqual(projected_residual(F(1), F(-2), F(1, 4), F(0), F(1)), 0)

    def test_interior_projected_residual(self):
        self.assertEqual(projected_residual(F(1), F(0), F(1, 2), F(0), F(2)), 0)

    def test_positive_residual_nonoptimum(self):
        self.assertNotEqual(projected_residual(F(3, 2), F(2), F(1, 4), F(0), F(2)), 0)

    def test_eta_must_be_positive(self):
        with self.assertRaises(ValueError): projected_residual(0, 0, 0, 0, 1)

    def test_distance_gradient_bound(self):
        for a in range(1, 6):
            for r in range(-2, 3):
                for x in range(-4, 5):
                    self.assertLessEqual(abs(F(x-r)), abs(derivative(F(a), F(r), F(x)))/F(2*a))

    def test_gap_upper_bound(self):
        for a in range(1, 6):
            for r in range(-2, 3):
                for x in range(-4, 5):
                    gap = quadratic(F(a), F(r), F(0), F(x))
                    g = derivative(F(a), F(r), F(x))
                    self.assertEqual(gap, g*g/F(4*a))

    def test_gap_lower_bound(self):
        for a in range(1, 6):
            for x in range(-3, 4):
                self.assertEqual(quadratic(F(a), F(0), F(0), F(x)), F(2*a)*x*x/2)

    def test_derivative_localization_exact_quadratic(self):
        for a in range(1, 5):
            for r in range(-2, 3):
                lo, hi = F(r-2), F(r+3)
                gl = derivative(F(a), F(r), lo)
                gu = derivative(F(a), F(r), hi)
                left, right = derivative_localization(gl, gu, F(2*a), F(2*a), lo, hi)
                self.assertEqual((left, right), (F(r), F(r)))

    def test_derivative_localization_unequal_bounds(self):
        # f(x)=x^4+x^2, f'' in [2,14] on [-1,1]
        l, u = derivative_localization(F(-6), F(6), F(2), F(14), F(-1), F(1))
        self.assertLessEqual(l, 0)
        self.assertGreaterEqual(u, 0)

    def test_derivative_localization_invalid(self):
        with self.assertRaises(ValueError): derivative_localization(1, -1, 1, 2, -1, 1)

    def test_bisection_halves_length(self):
        g = lambda x: 2*(x-F(3, 7))
        for n in range(8):
            l, u = bisect_derivative(g, F(0), F(1), n)
            self.assertLessEqual(u-l, F(1, 2**n))
            self.assertLessEqual(l, F(3, 7))
            self.assertGreaterEqual(u, F(3, 7))

    def test_bisection_early_zero(self):
        self.assertEqual(bisect_derivative(lambda x: 2*(x-1), F(0), F(2), 8), (F(1), F(1)))

    def test_bisection_invalid(self):
        with self.assertRaises(ValueError): bisect_derivative(lambda x: x+1, F(0), F(1), 2)

    def test_bisection_negative_steps(self):
        with self.assertRaises(ValueError): bisect_derivative(lambda x: x, F(-1), F(1), -1)

    def test_bisection_value_bound(self):
        g = lambda x: 2*(x-F(3, 7))
        for n in range(8):
            l, u = bisect_derivative(g, F(0), F(1), n)
            c = (l+u)/2
            self.assertLessEqual((c-F(3, 7))**2, F(2)*(u-l)**2/8)
