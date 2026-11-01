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

    def test_tangent_lower_bound_exact(self):
        for a in range(1, 5):
            for r in range(-2, 3):
                for c in range(-2, 3):
                    lo, hi = F(-3), F(3)
                    f_c = quadratic(F(a), F(r), F(1), F(c))
                    g_c = derivative(F(a), F(r), F(c))
                    lower = quadratic_lower_bound(f_c, g_c, F(2*a), F(c), lo, hi)
                    z = project(F(r), lo, hi)
                    self.assertEqual(lower, quadratic(F(a), F(r), F(1), z))

    def test_tangent_lower_bound_nonlinear(self):
        f = lambda x: x**4+x*x
        g = lambda x: 4*x**3+2*x
        lo, hi, c = F(-1), F(1), F(1, 2)
        lower = quadratic_lower_bound(f(c), g(c), F(2), c, lo, hi)
        for j in range(-20, 21):
            self.assertLessEqual(lower, f(F(j, 20)))

    def test_lower_bound_invalid_curvature(self):
        with self.assertRaises(ValueError): quadratic_lower_bound(0, 0, 0, 0, -1, 1)

    def test_lower_bound_invalid_center(self):
        with self.assertRaises(ValueError): quadratic_lower_bound(0, 0, 1, 3, -1, 1)

    def test_prune_strict(self):
        self.assertTrue(can_prune(F(5), F(3)))

    def test_prune_tie_not_safe(self):
        self.assertFalse(can_prune(F(0), F(0)))

    def test_prune_lower_not_enough(self):
        self.assertFalse(can_prune(F(2), F(3)))

    def test_noisy_gradient_distance(self):
        m, true_g, measured, delta = F(4), F(1, 4), F(1, 5), F(1, 10)
        self.assertLessEqual(abs(true_g)/m, (abs(measured)+delta)/m)
        self.assertLessEqual(abs(true_g-measured), delta)

    def test_noisy_gradient_gap(self):
        g, measured, delta, m = F(1, 4), F(1, 5), F(1, 10), F(4)
        self.assertLessEqual(g*g/(2*m), (abs(measured)+delta)**2/(2*m))

    def test_noisy_sign_bracket(self):
        ml, mu, dl, du = F(-3), F(5), F(1), F(1)
        self.assertLessEqual(ml+dl, 0)
        self.assertGreaterEqual(mu-du, 0)

    def test_noisy_sign_bracket_not_certified(self):
        ml, mu, dl, du = F(-1, 10), F(1, 10), F(1, 5), F(1, 5)
        self.assertGreater(ml+dl, 0)
        self.assertLess(mu-du, 0)

    def test_gap_to_distance(self):
        eps, m = F(1, 50), F(4)
        self.assertEqual(2*eps/m, F(1, 100))

    def test_endpoint_gap_bound(self):
        # f=x+x², x*=0, f'(0)=1, m=2; T5 still holds at the boundary.
        for j in range(11):
            x = F(j, 10)
            f = x+x*x
            g = 1+2*x
            self.assertLessEqual(f, g*g/F(4))
            self.assertGreaterEqual(f, x*x)

    def test_strict_pruning_counterexample(self):
        for j in range(11):
            self.assertEqual(F(0), F(0)*j)
        self.assertFalse(can_prune(0, 0))

    def test_wrong_curvature_counterexample(self):
        f = lambda x: -x*x
        self.assertLess(f(F(1)), f(F(0)))

    def test_small_gap_large_distance_counterexample(self):
        for k in range(1, 8):
            eps = F(1, 10**k)
            self.assertEqual(eps*F(1)**2, eps)
            self.assertEqual(abs(F(1)-F(0)), 1)

    def test_z1(self):
        self.assertEqual(quadratic(F(3), F(2), F(7), F(2)), 7)

    def test_z5(self):
        self.assertEqual(derivative_localization(F(-2), F(4), F(2), F(2), F(0), F(3)), (F(1), F(1)))

    def test_z7(self):
        self.assertEqual(quadratic_lower_bound(F(5), F(4), F(4), F(2), F(2), F(3)), F(5))

    def test_z9(self):
        self.assertEqual((F(1, 5)+F(1, 10))/F(4), F(3, 40))
        self.assertEqual((F(3, 10)**2)/(F(8)), F(9, 800))

    def test_z11(self):
        self.assertEqual(2*F(1, 50)/F(4), F(1, 100))

    def test_z12(self):
        self.assertEqual(F(8)*F(1, 2)**2/F(8), F(1, 4))


if __name__ == '__main__':
    unittest.main()
