"""Exact finite verification of F25.1 certificates; not a formal proof of theorems."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import unittest


def bisect_sqrt2(steps: int) -> tuple[F, F]:
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    lo, hi = F(1), F(2)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if mid * mid < 2:
            lo = mid
        elif mid * mid > 2:
            hi = mid
        else:
            raise AssertionError("sqrt(2) cannot be rational")
    return lo, hi


def newton_sqrt2(x: F) -> F:
    if x <= 0:
        raise ValueError("positive starting point required")
    return (x + 2 / x) / 2


def residual_certificate(q: F) -> F:
    if q <= 0:
        raise ValueError("positive rational q required")
    return abs(q * q - 2) / q


def multiply_certificates(p: F, e: F, q: F, f: F) -> tuple[F, F]:
    if e < 0 or f < 0:
        raise ValueError("error bounds must be nonnegative")
    return p * q, abs(p) * f + abs(q) * e + e * f


def separated_inverse(a: F, b: F, c: F) -> bool:
    if c <= 0 or abs(a) < c or abs(b) < c:
        raise ValueError("not separated from zero")
    return abs(1 / a - 1 / b) <= abs(a - b) / (c * c)


def is_nested(intervals: list[tuple[F, F]]) -> bool:
    if not intervals:
        return False
    if any(lo > hi for lo, hi in intervals):
        return False
    return all(prev_lo <= lo and hi <= prev_hi
               for (prev_lo, prev_hi), (lo, hi) in zip(intervals, intervals[1:]))


def sign_certificate(lo: F, hi: F) -> int | None:
    if lo > hi:
        raise ValueError("invalid interval")
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    return None


class TestF251(unittest.TestCase):
    def test_01_initial_bisection(self):
        self.assertEqual(bisect_sqrt2(0), (F(1), F(2)))

    def test_02_bisection_step_1(self):
        self.assertEqual(bisect_sqrt2(1), (F(1), F(3, 2)))

    def test_03_bisection_step_2(self):
        self.assertEqual(bisect_sqrt2(2), (F(5, 4), F(3, 2)))

    def test_04_bisection_step_3(self):
        self.assertEqual(bisect_sqrt2(3), (F(11, 8), F(3, 2)))

    def test_05_bisection_step_4(self):
        self.assertEqual(bisect_sqrt2(4), (F(11, 8), F(23, 16)))

    def test_06_bisection_widths(self):
        for n in range(0, 24):
            lo, hi = bisect_sqrt2(n)
            self.assertEqual(hi - lo, F(1, 2**n))

    def test_07_bisection_squared_sign(self):
        for n in range(0, 24):
            lo, hi = bisect_sqrt2(n)
            self.assertLess(lo * lo, 2)
            self.assertGreater(hi * hi, 2)

    def test_08_bisection_residual(self):
        for n in range(0, 24):
            lo, _ = bisect_sqrt2(n)
            self.assertLessEqual(2 - lo * lo, F(4, 2**n))

    def test_09_bisection_nested(self):
        self.assertTrue(is_nested([bisect_sqrt2(n) for n in range(0, 24)]))

    def test_10_bisection_reject_negative_steps(self):
        with self.assertRaises(ValueError):
            bisect_sqrt2(-1)

    def test_11_newton_three_steps(self):
        x = F(1)
        expected = [F(3, 2), F(17, 12), F(577, 408)]
        for target in expected:
            x = newton_sqrt2(x)
            self.assertEqual(x, target)

    def test_12_newton_residual_identity(self):
        for numerator in range(1, 11):
            for denominator in range(1, 8):
                x = F(numerator, denominator)
                y = newton_sqrt2(x)
                self.assertEqual(y * y - 2, (x * x - 2)**2 / (4*x*x))

    def test_13_newton_above_root(self):
        for x in [F(1, 10), F(1), F(2), F(17, 12), F(100)]:
            y = newton_sqrt2(x)
            self.assertGreater(y * y, 2)

    def test_14_newton_reject_nonpositive(self):
        for x in [F(0), F(-1)]:
            with self.assertRaises(ValueError):
                newton_sqrt2(x)

    def test_15_rational_bracket_141(self):
        self.assertEqual(F(141, 100)**2, F(19881, 10000))
        self.assertEqual(F(71, 50)**2, F(20164, 10000))

    def test_16_rational_bracket_7_5(self):
        self.assertEqual(F(7, 5)**2 - 2, F(-1, 25))
        self.assertEqual(F(3, 2)**2 - 2, F(1, 4))

    def test_17_residual_certificate_3_2(self):
        self.assertEqual(residual_certificate(F(3, 2)), F(1, 6))

    def test_18_residual_cert_reject_nonpositive(self):
        for q in [F(0), F(-1)]:
            with self.assertRaises(ValueError):
                residual_certificate(q)

    def test_19_residual_cert_vs_bisection(self):
        # Each interval encloses the root; exact arithmetic bounds the error.
        for n in range(2, 18):
            lo, hi = bisect_sqrt2(n)
            for q in [lo, hi]:
                e = residual_certificate(q)
                self.assertGreaterEqual(q + e, lo)
                self.assertLessEqual(q - e, hi)

    def test_20_cauchy_modulus_one_over_n(self):
        for k in range(1, 12):
            N = 2**k
            for n, m in product(range(N, N+5), repeat=2):
                self.assertLessEqual(abs(F(1, n)-F(1, m)), F(1, 2**k))

    def test_21_alternating_modulus(self):
        for k in range(1, 9):
            N = 2**(k+1)
            for n, m in product(range(N, N+5), repeat=2):
                a, b = 1+F((-1)**n, n), 1+F((-1)**m, m)
                self.assertLessEqual(abs(a-b), F(1, 2**k))

    def test_22_equivalent_representatives(self):
        for n in range(1, 500):
            a, b = 1+F(1,n), 1+F((-1)**n,n)
            self.assertLessEqual(abs(a-b), F(2,n))

    def test_23_stability_by_fast_perturbation(self):
        for n in range(1, 30):
            a = F(1) + F(1, n)
            b = a + F((-1)**n, 2**n)
            self.assertLessEqual(abs(a-b), F(1, 2**n))

    def test_24_multiply_certificate_example(self):
        self.assertEqual(multiply_certificates(F(2), F(1,10), F(-3), F(1,20)),
                         (F(-6), F(81,200)))

    def test_25_multiply_certificates_exhaustive(self):
        for p, q in product(range(-3, 4), repeat=2):
            for dp, dq in product([F(-1,10), F(0), F(1,10)], repeat=2):
                center, error = multiply_certificates(F(p), F(1,10), F(q), F(1,10))
                self.assertLessEqual(abs((p+dp)*(q+dq)-center), error)

    def test_26_multiply_reject_negative_errors(self):
        with self.assertRaises(ValueError):
            multiply_certificates(F(1), F(-1), F(2), F(0))

    def test_27_inverse_bound(self):
        for a, b in product([F(1), F(2), F(3), F(4), F(5)], repeat=2):
            self.assertTrue(separated_inverse(a, b, F(1)))

    def test_28_inverse_negative_bound(self):
        for a, b in product([F(-1), F(-2), F(-3)], repeat=2):
            self.assertTrue(separated_inverse(a, b, F(1)))

    def test_29_inverse_reject_zero(self):
        with self.assertRaises(ValueError):
            separated_inverse(F(0), F(1), F(1))

    def test_30_inverse_2_plus_one_over_n(self):
        for n in range(1, 100):
            a = F(2) + F(1,n)
            self.assertEqual(abs(1/a - F(1,2)), F(1,2*(2*n+1)))

    def test_31_sign_positive(self):
        self.assertEqual(sign_certificate(F(1,10), F(2)), 1)

    def test_32_sign_negative(self):
        self.assertEqual(sign_certificate(F(-2), F(-1,10)), -1)

    def test_33_sign_undetermined(self):
        self.assertIsNone(sign_certificate(F(-1), F(1)))

    def test_34_sign_reject_bad_interval(self):
        with self.assertRaises(ValueError):
            sign_certificate(F(2), F(1))

    def test_35_shrinking_not_nested(self):
        intervals = [(F((-1)**n), F((-1)**n) + F(1,2**n)) for n in range(1,10)]
        self.assertFalse(is_nested(intervals))

    def test_36_fast_prefix_ambiguity(self):
        N = 3
        z = [F(0) for _ in range(12)]
        b = [F(0) if n <= N else F(1,16) for n in range(1,13)]
        self.assertEqual(z[:N], b[:N])
        for n in range(1,13):
            for m in range(n,13):
                self.assertLessEqual(abs(b[m-1]-b[n-1]), F(1,2**n))
        self.assertNotEqual(z[-1], b[-1])

    def test_37_rational_one_nested(self):
        intervals = [(F(1), F(1)+F(1,2**n)) for n in range(1,15)]
        self.assertTrue(is_nested(intervals))
        self.assertTrue(all(lo <= 1 <= hi for lo,hi in intervals))

    def test_38_diagonal_bound_finite(self):
        # x_n=1+2^-n, q_n=x_n+2^-n, limit=1; finite instance of T9.
        for n in range(1, 30):
            x_n = F(1) + F(1,2**n)
            q_n = x_n + F(1,2**n)
            self.assertLessEqual(abs(q_n-x_n), F(1,2**n))
            self.assertLessEqual(abs(F(1)-x_n), F(2,2**n))

    def test_39_lipschitz_example(self):
        # f(q)=3q+1 extends to the completion with L=3.
        for a, b in product([F(-3,2), F(0), F(2,3), F(5)], repeat=2):
            self.assertLessEqual(abs((3*a+1)-(3*b+1)), 3*abs(a-b))

    def test_40_non_cauchy_alternating(self):
        for N in range(1, 20):
            self.assertEqual(abs((-1)**N-(-1)**(N+1)), 2)


if __name__ == "__main__":
    unittest.main()
