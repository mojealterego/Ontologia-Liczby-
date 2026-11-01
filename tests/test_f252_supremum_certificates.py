"""Exact arithmetic regression for F25.2 certified supremum bounds.

Finite tests check implementations and counterexamples, not universal proofs.
Run: python -m unittest -v tests/test_f252_supremum_certificates.py
     python -m pytest -q tests/test_f252_supremum_certificates.py
"""
from __future__ import annotations

import unittest
from fractions import Fraction as F
from itertools import product


def grid(a: F, b: F, n: int) -> tuple[F, ...]:
    if not isinstance(n, int) or n < 0 or a >= b:
        raise ValueError("expected n>=0 and a<b")
    h = (b - a) / (2**n)
    return tuple(a + j * h for j in range(2**n + 1))


def certificate(samples: tuple[tuple[F, F], ...], L: F, h: F) -> tuple[F, F]:
    if not samples or L < 0 or h <= 0 or any(e < 0 for _, e in samples):
        raise ValueError("invalid certificate inputs")
    return (
        max(q - e for q, e in samples),
        max(q + e for q, e in samples) + L * h / 2,
    )


def exact_certificate(f, a: F, b: F, n: int, L: F) -> tuple[F, F]:
    xs = grid(a, b, n)
    return certificate(tuple((f(x), F(0)) for x in xs), L, (b - a) / (2**n))


def local_cone(left: tuple[F, F], right: tuple[F, F], L: F, width: F) -> F:
    if L < 0 or width <= 0 or left[1] < 0 or right[1] < 0:
        raise ValueError("invalid local bound")
    return max(left[0] + left[1], right[0] + right[1]) + L * width / 2


def finite_hausdorff(a: tuple[F, ...], b: tuple[F, ...]) -> F:
    if not a or not b:
        raise ValueError("nonempty sets required")
    return max(
        max(min(abs(x - y) for y in b) for x in a),
        max(min(abs(y - x) for x in a) for y in b),
    )


def tent(x: F) -> F:
    return 1 - abs(2 * x - 1)


def quadratic(x: F) -> F:
    return x * (1 - x)


class SupremumCertificateTests(unittest.TestCase):
    def test_01_grid_endpoints(self):
        self.assertEqual(grid(F(1, 3), F(4, 3), 2), (F(1, 3), F(7, 12), F(5, 6), F(13, 12), F(4, 3)))

    def test_02_grid_nested(self):
        for n in range(7):
            self.assertTrue(set(grid(F(0), F(1), n)).issubset(grid(F(0), F(1), n + 1)))

    def test_03_grid_spacing(self):
        for n in range(6):
            xs = grid(F(-2), F(3), n)
            self.assertTrue(all(y - x == F(5, 2**n) for x, y in zip(xs, xs[1:])))

    def test_04_grid_bad_n(self):
        with self.assertRaises(ValueError):
            grid(F(0), F(1), -1)

    def test_05_grid_bad_interval(self):
        with self.assertRaises(ValueError):
            grid(F(1), F(1), 2)

    def test_06_linear_z1(self):
        self.assertEqual(exact_certificate(lambda x: x, F(0), F(1), 1, F(1)), (F(1), F(5, 4)))

    def test_07_tent_z2(self):
        self.assertEqual(exact_certificate(tent, F(0), F(1), 0, F(2)), (F(0), F(1)))

    def test_08_quadratic_z3(self):
        self.assertEqual(exact_certificate(quadratic, F(0), F(1), 1, F(1)), (F(1, 4), F(1, 2)))

    def test_09_exact_rate_z4(self):
        self.assertEqual(min(n for n in range(20) if F(2, 2**(n + 1)) <= F(1, 64)), 6)

    def test_10_inexact_z5(self):
        xs = grid(F(0), F(1), 2)
        B, C = certificate(tuple((x, F(1, 100)) for x in xs), F(1), F(1, 4))
        self.assertEqual((B, C, C - B), (F(99, 100), F(227, 200), F(29, 200)))

    def test_11_width_z6(self):
        self.assertEqual(2 * F(1, 100) + F(2) * F(1, 16) / 2, F(33, 400))

    def test_12_function_stability_z7(self):
        xs = grid(F(0), F(1), 5)
        f = lambda x: x
        g = lambda x: x + F(1, 5)
        self.assertEqual(abs(max(map(f, xs)) - max(map(g, xs))), F(1, 5))

    def test_13_domain_stability_z8(self):
        A = (F(0), F(1, 2))
        B = (F(1, 2), F(1))
        self.assertEqual(finite_hausdorff(A, B), F(1, 2))
        self.assertEqual(abs(max(A) - max(B)), F(1, 2))

    def test_14_local_cone_z9(self):
        self.assertEqual(local_cone((F(1, 4), F(0)), (F(1, 2), F(0)), F(1), F(1, 4)), F(5, 8))

    def test_15_pruning_z10(self):
        self.assertLess(F(2, 3), F(3, 4))

    def test_16_approx_argmax_z11(self):
        self.assertEqual(F(1, 2) / 2 + 2 * F(1, 100), F(27, 100))

    def test_17_continuous_spike_z12(self):
        for H in (F(1, 3), F(2), F(17, 5)):
            f = lambda x: 4 * H * min(x, 1 - x)
            self.assertEqual((f(F(0)), f(F(1)), f(F(1, 2))), (0, 0, 2 * H))

    def test_18_tent_wrong_lipschitz_K5(self):
        B, C = exact_certificate(tent, F(0), F(1), 0, F(1))
        self.assertEqual((B, C), (F(0), F(1, 2)))
        self.assertGreater(tent(F(1, 2)), C)

    def test_19_tent_correct_lipschitz(self):
        for n in range(8):
            B, C = exact_certificate(tent, F(0), F(1), n, F(2))
            self.assertLessEqual(B, F(1))
            self.assertGreaterEqual(C, F(1))

    def test_20_quadratic_correct_lipschitz(self):
        for n in range(8):
            B, C = exact_certificate(quadratic, F(0), F(1), n, F(1))
            self.assertLessEqual(B, F(1, 4))
            self.assertGreaterEqual(C, F(1, 4))

    def test_21_linear_certificates_on_rational_intervals(self):
        for a, b in ((F(-2), F(3)), (F(1, 7), F(9, 7)), (F(-5, 4), F(-1, 4))):
            for n in range(6):
                B, C = exact_certificate(lambda x: 3*x+2, a, b, n, F(3))
                self.assertLessEqual(B, 3*b+2)
                self.assertGreaterEqual(C, 3*b+2)

    def test_22_decreasing_linear(self):
        for n in range(7):
            B, C = exact_certificate(lambda x: -2*x+3, F(0), F(1), n, F(2))
            self.assertEqual(B, F(3))
            self.assertGreaterEqual(C, F(3))

    def test_23_constant_function(self):
        for n in range(7):
            B, C = exact_certificate(lambda x: F(7, 11), F(-1), F(2), n, F(0))
            self.assertEqual((B, C), (F(7, 11), F(7, 11)))

    def test_24_noisy_samples_sound(self):
        for n in range(5):
            xs = grid(F(0), F(1), n)
            h = F(1, 2**n)
            for bias in (F(-1, 100), F(0), F(1, 100)):
                B, C = certificate(tuple((tent(x) + bias, F(1, 100)) for x in xs), F(2), h)
                self.assertLessEqual(B, F(1))
                self.assertGreaterEqual(C, F(1))

    def test_25_width_bound_exact(self):
        for n in range(7):
            B, C = exact_certificate(tent, F(0), F(1), n, F(2))
            self.assertLessEqual(C-B, F(2, 2**(n+1)))

    def test_26_width_bound_noisy(self):
        for n in range(6):
            xs = grid(F(0), F(1), n)
            B, C = certificate(tuple((quadratic(x), F(1, 100)) for x in xs), F(1), F(1, 2**n))
            self.assertLessEqual(C-B, F(1, 50) + F(1, 2**(n+1)))

    def test_27_monotone_grid_max(self):
        vals = [max(tent(x) for x in grid(F(0), F(1), n)) for n in range(7)]
        self.assertEqual(vals, sorted(vals))
        self.assertEqual(vals[1:], [F(1)]*6)

    def test_28_local_cone_sound_for_linear(self):
        for u, v in ((F(0), F(1, 3)), (F(1, 4), F(1, 2)), (F(-1), F(2))):
            C = local_cone((u, F(0)), (v, F(0)), F(1), v-u)
            for j in range(33):
                x = u + (v-u)*F(j, 32)
                self.assertLessEqual(x, C)

    def test_29_local_cone_sound_for_tent(self):
        for n in range(1, 6):
            xs = grid(F(0), F(1), n)
            for u, v in zip(xs, xs[1:]):
                C = local_cone((tent(u), F(0)), (tent(v), F(0)), F(2), v-u)
                for j in range(17):
                    x = u+(v-u)*F(j, 16)
                    self.assertLessEqual(tent(x), C)

    def test_30_parameter_monotonicity(self):
        samples = ((F(1, 4), F(1, 100)), (F(3, 4), F(1, 100)))
        B, C = certificate(samples, F(1), F(1, 2))
        B2, C2 = certificate(tuple((q, e + F(1, 50)) for q, e in samples), F(2), F(1, 2))
        self.assertLessEqual(B2, B)
        self.assertGreaterEqual(C2, C)

    def test_31_reject_negative_error(self):
        with self.assertRaises(ValueError):
            certificate(((F(0), F(-1)),), F(1), F(1))

    def test_32_reject_negative_lipschitz(self):
        with self.assertRaises(ValueError):
            certificate(((F(0), F(0)),), F(-1), F(1))

    def test_33_reject_empty_samples(self):
        with self.assertRaises(ValueError):
            certificate((), F(1), F(1))

    def test_34_reject_empty_hausdorff(self):
        with self.assertRaises(ValueError):
            finite_hausdorff((), (F(1),))

    def test_35_hausdorff_symmetry(self):
        sets = ((F(0), F(1, 2)), (F(1, 3), F(2, 3)), (F(1),))
        for a, b in product(sets, repeat=2):
            self.assertEqual(finite_hausdorff(a, b), finite_hausdorff(b, a))

    def test_36_hausdorff_triangle(self):
        sets = ((F(0), F(1, 2)), (F(1, 3), F(2, 3)), (F(1),))
        for a, b, c in product(sets, repeat=3):
            self.assertLessEqual(finite_hausdorff(a, c), finite_hausdorff(a, b)+finite_hausdorff(b, c))

    def test_37_finite_domain_stability(self):
        sets = ((F(0), F(1, 2)), (F(1, 3), F(2, 3)), (F(1),))
        for a, b in product(sets, repeat=2):
            self.assertLessEqual(abs(max(a)-max(b)), finite_hausdorff(a, b))

    def test_38_approx_argmax_bound(self):
        for n in range(1, 6):
            xs = grid(F(0), F(1), n)
            eta = F(1, 100)
            q = {x: tent(x) + (eta if j%2 else -eta) for j,x in enumerate(xs)}
            xstar = max(xs, key=lambda x:q[x])
            self.assertLessEqual(F(1)-tent(xstar), F(2, 2**(n+1)) + 2*eta)

    def test_39_nested_tolerance(self):
        delta = F(1, 16)
        eta = F(1, 64)
        n = 5
        self.assertLessEqual(eta, delta/4)
        self.assertLessEqual(F(2, 2**(n+1)), delta/2)
        xs = grid(F(0), F(1), n)
        B, C = certificate(tuple((tent(x), eta) for x in xs), F(2), F(1, 2**n))
        self.assertLessEqual(C-B, delta)

    def test_40_wrong_sample_error_not_certified(self):
        B, C = certificate(((F(0), F(0)), (F(0), F(0))), F(0), F(1))
        self.assertEqual((B, C), (F(0), F(0)))
        self.assertNotIn(F(1), (B, C))  # f=1 violates the sample assumption


if __name__ == "__main__":
    unittest.main()
