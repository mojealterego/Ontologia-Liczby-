"""F27.2: exact rational checks of epsilon-N certificates (not proof mechanization)."""
from fractions import Fraction as F
from itertools import product
from math import floor
import unittest


def rational_reciprocal_modulus(epsilon: F) -> int:
    """For 1/(n+1) < epsilon, n >= floor(1/epsilon) is sufficient."""
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    return (1 / epsilon).numerator // (1 / epsilon).denominator


def sum_modulus(ma, mb, epsilon: F) -> int:
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    return max(ma(epsilon / 2), mb(epsilon / 2))


def product_modulus(ma, mb, A: F, B: F, epsilon: F) -> int:
    if epsilon <= 0 or A < 0 or B < 0:
        raise ValueError("invalid bounds")
    return max(mb(epsilon / (2 * max(F(1), A))),
               ma(epsilon / (2 * max(F(1), B))))


def quotient_modulus(ma, mb, a: F, beta: F, epsilon: F) -> int:
    if epsilon <= 0 or beta <= 0:
        raise ValueError("invalid epsilon or denominator margin")
    c1, c2 = 2 / beta, 2 * abs(a) / beta**2
    return max(mb(beta / 2),
               ma(epsilon / (2 * max(F(1), c1))),
               mb(epsilon / (2 * max(F(1), c2))))


def homographic_error(a: F, b: F, c: F, d: F, n: int) -> F:
    if c == 0 or c * n + d == 0:
        raise ZeroDivisionError
    return abs(b * c - a * d) / (abs(c) * abs(c * n + d))


def power_rate_modulus(C: F, p: int, epsilon: F) -> int:
    """Exact minimal integer threshold for C/(n+1)^p < epsilon."""
    if C <= 0 or p <= 0 or epsilon <= 0:
        raise ValueError("invalid certificate")
    n = 0
    while C >= epsilon * (n + 1)**p:
        n += 1
    return n


def window_ok(sequence, n: int, g, epsilon: F) -> bool:
    if epsilon <= 0:
        raise ValueError
    window = [sequence(i) for i in range(n, n + g(n) + 1)]
    return max(window) - min(window) < epsilon


def monotone_candidates(A: F, B: F, epsilon: F, g):
    if A > B or epsilon <= 0:
        raise ValueError
    K = int((B - A) // epsilon) + 1
    n = 0
    out = []
    for _ in range(K):
        out.append(n)
        n = n + g(n) + 1
    return out


class LimitWitnesses(unittest.TestCase):
    def test_reciprocal_strict_boundary(self):
        self.assertEqual(rational_reciprocal_modulus(F(1, 5)), 5)
        self.assertEqual(rational_reciprocal_modulus(F(2)), 0)

    def test_reciprocal_exhaustive(self):
        for numerator in range(1, 11):
            for denominator in range(1, 13):
                eps = F(numerator, denominator)
                N = rational_reciprocal_modulus(eps)
                self.assertLess(F(1, N + 1), eps)
                if N > 0:
                    self.assertGreaterEqual(F(1, N), eps)

    def test_reciprocal_invalid(self):
        for eps in [F(0), F(-1, 10)]:
            with self.assertRaises(ValueError):
                rational_reciprocal_modulus(eps)

    def test_sum_modulus(self):
        for eps in [F(1, 3), F(1, 50), F(3, 2)]:
            N = sum_modulus(rational_reciprocal_modulus,
                            lambda e: rational_reciprocal_modulus(e / 2), eps)
            for n in range(N, N + 20):
                self.assertLess(F(3, n + 1), eps)

    def test_product_modulus(self):
        for eps in [F(1, 2), F(1, 10), F(1, 100)]:
            N = product_modulus(rational_reciprocal_modulus,
                                rational_reciprocal_modulus, F(1), F(2), eps)
            for n in range(N, N + 25):
                a = F(1, n + 1)
                b = F(2) + F(1, n + 1)
                self.assertLess(abs(a * b), eps)

    def test_product_zero_bounds(self):
        self.assertGreaterEqual(product_modulus(lambda _: 0, lambda _: 0,
                                                F(0), F(0), F(1)), 0)

    def test_product_invalid(self):
        with self.assertRaises(ValueError):
            product_modulus(lambda _: 0, lambda _: 0, F(-1), F(1), F(1))

    def test_quotient_modulus(self):
        for eps in [F(1, 10), F(1, 100), F(2)]:
            N = quotient_modulus(rational_reciprocal_modulus,
                                 rational_reciprocal_modulus, F(1), F(2), eps)
            for n in range(N, N + 30):
                a, b = F(1) + F(1, n + 1), F(2) + F(1, n + 1)
                self.assertLess(abs(a / b - F(1, 2)), eps)
                self.assertGreater(abs(b), F(1))

    def test_quotient_invalid_margin(self):
        with self.assertRaises(ValueError):
            quotient_modulus(lambda _: 0, lambda _: 0, F(1), F(0), F(1))

    def test_homography_exact(self):
        for a, b, c, d in product(range(-3, 4), repeat=4):
            if c == 0:
                continue
            for n in [1, 2, 4, 10]:
                if c * n + d == 0:
                    continue
                x = (F(a * n + b) / F(c * n + d))
                self.assertEqual(abs(x - F(a, c)),
                                 homographic_error(F(a), F(b), F(c), F(d), n))

    def test_homography_upper_bound(self):
        for a, b, c, d in product(range(-2, 3), repeat=4):
            if c == 0:
                continue
            for n in range(1, 13):
                if F(n) < F(2 * abs(d), abs(c)):
                    continue
                self.assertLessEqual(homographic_error(F(a), F(b), F(c), F(d), n),
                                     F(2 * abs(b * c - a * d), c * c * n))

    def test_homography_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            homographic_error(F(1), F(2), F(1), F(-2), 2)

    def test_power_modulus_exact(self):
        for C in [F(1), F(5), F(7, 3)]:
            for p in [1, 2, 3]:
                for eps in [F(1, 5), F(1, 100), F(2)]:
                    N = power_rate_modulus(C, p, eps)
                    self.assertLess(C / (N + 1)**p, eps)
                    if N > 0:
                        self.assertGreaterEqual(C / N**p, eps)

    def test_power_invalid(self):
        for C, p, eps in [(F(0), 2, F(1)), (F(1), 0, F(1)), (F(1), 2, F(0))]:
            with self.assertRaises(ValueError):
                power_rate_modulus(C, p, eps)

    def test_monotone_metastability_exhaustive(self):
        g = lambda n: n % 3 + 1
        for values in product([F(0), F(1, 4), F(1, 2), F(3, 4), F(1)], repeat=4):
            if list(values) != sorted(values):
                continue
            seq = lambda n, vals=values: vals[min(n, len(vals) - 1)]
            for eps in [F(1, 4), F(1, 2), F(3, 2)]:
                cand = monotone_candidates(F(0), F(1), eps, g)
                self.assertTrue(any(window_ok(seq, n, g, eps) for n in cand))

    def test_monotone_specific_example(self):
        g = lambda _: 2
        seq = lambda n: F(1) - F(1, n + 1)
        self.assertEqual(monotone_candidates(F(0), F(1), F(1, 4), g),
                         [0, 3, 6, 9, 12])
        self.assertTrue(window_ok(seq, 3, g, F(1, 4)))

    def test_window_zero_vacuous(self):
        self.assertTrue(window_ok(lambda n: F((-1)**n), 0, lambda _: 0, F(1, 2)))

    def test_window_detects_oscillation(self):
        self.assertFalse(window_ok(lambda n: F((-1)**n), 0, lambda _: 1, F(1)))

    def test_window_invalid(self):
        with self.assertRaises(ValueError):
            window_ok(lambda _: F(0), 0, lambda _: 1, F(0))

    def test_finite_prefix_counterexample(self):
        for m in [0, 10, 1000]:
            a = lambda n: 0
            b = lambda n: 0 if n <= m else (-1)**n
            self.assertTrue(all(a(n) == b(n) for n in range(m + 1)))
            self.assertNotEqual(b(m + 2), b(m + 3))

    def test_pointwise_not_uniform(self):
        for n in range(30):
            self.assertEqual(max(int(n == k) for k in range(30)), 1)
        for k in range(30):
            self.assertEqual(sum(int(n == k) for n in range(31, 60)), 0)

    def test_z1(self):
        self.assertEqual(min(n for n in range(1000) if F(7, n + 2) < F(1, 100)), 699)

    def test_z2(self):
        self.assertEqual(min(n for n in range(100) if F(1, n + 1) < F(1, 64)), 64)

    def test_z3(self):
        self.assertEqual(min(n for n in range(500)
                             if abs(F(3*n+2, 2*n+5)-F(3, 2)) < F(1, 100)), 273)

    def test_z4(self):
        self.assertEqual(min(n for n in range(100) if F(3, n + 1) < F(1, 10)), 30)

    def test_z5(self):
        for n in range(50, 100):
            t = F(1, n + 1)
            self.assertLess(abs((1 + t)*(2 - t) - 2), F(1, 50))

    def test_z6(self):
        for n in range(25, 75):
            self.assertLess(abs(1 / (F(2) + F(1, n+1)) - F(1, 2)), F(1, 100))

    def test_z7(self):
        self.assertEqual(power_rate_modulus(F(5), 2, F(1, 100)), 22)

    def test_z10(self):
        self.assertLess(F(1, 15), F(7, 100))
        self.assertEqual(2*15, 30)

    def test_z11(self):
        for n in range(100, 160):
            v = F(1, n+1) + F((-1)**n, (n+1)**2)
            self.assertLess(abs(v), F(1, 50))


if __name__ == '__main__':
    unittest.main()