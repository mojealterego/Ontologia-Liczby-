"""F21.3: deterministic checks for rational logarithm certificates.

Finite tests validate examples and algorithms, not every analytic proof.
"""
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from math import gcd
import unittest


def valuations(x: Fraction) -> dict[int, int]:
    if x <= 0:
        raise ValueError("requires a positive rational")
    d: dict[int, int] = {}
    for numerator, sign in ((x.numerator, 1), (x.denominator, -1)):
        n = numerator
        p = 2
        while p * p <= n:
            while n % p == 0:
                d[p] = d.get(p, 0) + sign
                n //= p
            p += 1
        if n > 1:
            d[n] = d.get(n, 0) + sign
    return {p: v for p, v in d.items() if v}


def rational_log(a: Fraction, x: Fraction) -> Fraction | None:
    if a <= 0 or a == 1 or x <= 0:
        raise ValueError("invalid real logarithm domain")
    av, xv = valuations(a), valuations(x)
    p = next(iter(av))
    m_n = Fraction(xv.get(p, 0), av[p])
    return m_n if all(Fraction(xv.get(q, 0)) == m_n * av.get(q, 0)
                      for q in set(av) | set(xv)) else None


def compare_to_rational(a: Fraction, x: Fraction, bound: Fraction) -> int:
    if a <= 0 or a == 1 or x <= 0:
        raise ValueError("invalid real logarithm domain")
    left, right = x ** bound.denominator, a ** bound.numerator
    sign = (left > right) - (left < right)
    return sign if a > 1 else -sign


def symmetric_parameter(y: Fraction) -> Fraction:
    if y < 1:
        raise ValueError("requires y >= 1")
    return (y - 1) / (y + 1)


def series_bounds(y: Fraction, n: int) -> tuple[Fraction, Fraction]:
    if y < 1 or n < 1:
        raise ValueError("requires y >= 1 and n >= 1")
    t = symmetric_parameter(y)
    s = 2 * sum((t ** (2*j+1) / (2*j+1) for j in range(n)), Fraction(0))
    e = 2 * t ** (2*n+1) / ((2*n+1) * (1-t*t))
    return s, s+e


def ln_bounds(x: Fraction, n: int) -> tuple[Fraction, Fraction]:
    if x <= 0:
        raise ValueError("requires x > 0")
    if x >= 1:
        return series_bounds(x, n)
    lo, hi = series_bounds(1/x, n)
    return -hi, -lo


def reduce_binary(y: Fraction) -> tuple[int, Fraction]:
    if y < 1:
        raise ValueError("requires y >= 1")
    k = 0
    z = y
    while z >= 2:
        z /= 2
        k += 1
    return k, z


def reduced_ln_bounds(x: Fraction, n: int) -> tuple[Fraction, Fraction]:
    if x <= 0:
        raise ValueError("requires x > 0")
    if x < 1:
        lo, hi = reduced_ln_bounds(1/x, n)
        return -hi, -lo
    k, z = reduce_binary(x)
    l2, u2 = series_bounds(Fraction(2), n)
    lz, uz = series_bounds(z, n)
    return k*l2 + lz, k*u2 + uz


def interval_divide(num: tuple[Fraction, Fraction], den: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    lo, hi = den
    if lo <= 0 <= hi:
        raise ZeroDivisionError("denominator interval contains zero")
    corners = [a / b for a in num for b in den]
    return min(corners), max(corners)


def decimal_value(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


class F213Tests(unittest.TestCase):
    def test_valuation_examples(self):
        self.assertEqual(valuations(Fraction(12, 5)), {2: 2, 3: 1, 5: -1})

    def test_valuation_multiplicative(self):
        xs = [Fraction(a, b) for a in range(1, 13) for b in range(1, 8)]
        for x in xs:
            for y in (Fraction(2, 3), Fraction(5, 4), Fraction(7, 1)):
                got = valuations(x*y)
                av, bv = valuations(x), valuations(y)
                want = {p: av.get(p, 0)+bv.get(p, 0) for p in set(av)|set(bv)}
                self.assertEqual(got, {p: v for p, v in want.items() if v})

    def test_rational_log_8_4(self):
        self.assertEqual(rational_log(Fraction(8), Fraction(4)), Fraction(2, 3))

    def test_rational_log_12_18_irrational(self):
        self.assertIsNone(rational_log(Fraction(12), Fraction(18)))

    def test_rational_log_2_3_irrational(self):
        self.assertIsNone(rational_log(Fraction(2), Fraction(3)))

    def test_rational_log_one(self):
        self.assertEqual(rational_log(Fraction(17, 4), Fraction(1)), Fraction(0))

    def test_rational_log_negative_exponent(self):
        self.assertEqual(rational_log(Fraction(1, 8), Fraction(4)), Fraction(-2, 3))

    def test_comparison_base_above_one(self):
        self.assertEqual(compare_to_rational(Fraction(2), Fraction(3), Fraction(3, 2)), 1)

    def test_comparison_base_below_one(self):
        self.assertEqual(compare_to_rational(Fraction(1, 2), Fraction(3), Fraction(-1)), -1)

    def test_comparison_equality(self):
        self.assertEqual(compare_to_rational(Fraction(8), Fraction(4), Fraction(2, 3)), 0)

    def test_series_ln_three_halves(self):
        self.assertEqual(series_bounds(Fraction(3, 2), 2),
                         (Fraction(152, 375), Fraction(152, 375)+Fraction(1, 7500)))

    def test_series_ln_two(self):
        self.assertEqual(series_bounds(Fraction(2), 2),
                         (Fraction(56, 81), Fraction(56, 81)+Fraction(1, 540)))

    def test_series_ln_two_error_four(self):
        lo, hi = series_bounds(Fraction(2), 4)
        self.assertEqual(hi-lo, Fraction(1, 78732))
        self.assertLess(hi-lo, Fraction(1, 10000))

    def test_inversion_symmetry(self):
        for x in [Fraction(1, 2), Fraction(2, 3), Fraction(1, 10)]:
            a, b = ln_bounds(x, 4)
            c, d = ln_bounds(1/x, 4)
            self.assertEqual((a, b), (-d, -c))

    def test_reduction(self):
        self.assertEqual(reduce_binary(Fraction(12)), (3, Fraction(3, 2)))
        self.assertEqual(reduce_binary(Fraction(2)), (1, Fraction(1)))

    def test_reduction_bound(self):
        for x in [Fraction(1), Fraction(2), Fraction(12), Fraction(127, 5), Fraction(1, 17)]:
            lo, hi = reduced_ln_bounds(x, 5)
            y = x if x >= 1 else 1/x
            k, _ = reduce_binary(y)
            cap = (k+1)*Fraction(9, 4*(2*5+1)*3**(2*5+1))
            self.assertLessEqual(hi-lo, cap)

    def test_decimal_containment(self):
        with localcontext() as ctx:
            ctx.prec = 75
            for x in [Fraction(1, 10), Fraction(2, 3), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3), Fraction(12), Fraction(100)]:
                lo, hi = reduced_ln_bounds(x, 8)
                target = decimal_value(x).ln()
                self.assertLessEqual(decimal_value(lo), target)
                self.assertLessEqual(target, decimal_value(hi))

    def test_interval_division(self):
        num = series_bounds(Fraction(3), 5)
        den = series_bounds(Fraction(2), 5)
        lo, hi = interval_divide(num, den)
        with localcontext() as ctx:
            ctx.prec = 70
            value = Decimal(3).ln() / Decimal(2).ln()
            self.assertLess(decimal_value(lo), value)
            self.assertLess(value, decimal_value(hi))

    def test_interval_denominator_zero(self):
        with self.assertRaises(ZeroDivisionError):
            interval_divide((Fraction(1), Fraction(2)), (Fraction(-1), Fraction(1)))

    def test_exact_difference_bounds(self):
        with localcontext() as ctx:
            ctx.prec = 75
            for a in range(1, 12):
                for b in range(a+1, 13):
                    difference = Decimal(b).ln()-Decimal(a).ln()
                    self.assertLess(decimal_value(Fraction(b-a, b)), difference)
                    self.assertLess(difference, decimal_value(Fraction(b-a, a)))

    def test_invalid_domains(self):
        for a, x in [(Fraction(1), Fraction(2)), (Fraction(-2), Fraction(3)), (Fraction(2), Fraction(0))]:
            with self.assertRaises(ValueError):
                rational_log(a, x)

    def test_width_monotonicity(self):
        for y in [Fraction(5, 4), Fraction(2), Fraction(3), Fraction(100)]:
            widths = [series_bounds(y, n)[1]-series_bounds(y, n)[0] for n in range(1, 7)]
            self.assertTrue(all(a > b for a, b in zip(widths, widths[1:])))


if __name__ == "__main__":
    unittest.main()


class F213AnalyticBoundsTests(unittest.TestCase):
    def test_log_one_plus_u_bounds(self):
        with localcontext() as ctx:
            ctx.prec = 75
            for u in [Fraction(-9, 10), Fraction(-1, 2), Fraction(-1, 10), Fraction(0), Fraction(1, 10), Fraction(2), Fraction(9)]:
                value = decimal_value(1+u).ln()
                self.assertLessEqual(decimal_value(u/(1+u)), value)
                self.assertLessEqual(value, decimal_value(u))

    def test_logsumexp_bound(self):
        with localcontext() as ctx:
            ctx.prec = 75
            for z in [(0,), (0, 0), (0, -1), (-3, -2, 0), (2, 2, 2)]:
                m = max(z)
                value = sum(Decimal(v).exp() for v in z).ln()
                self.assertLessEqual(Decimal(m), value)
                self.assertLessEqual(value, Decimal(m)+Decimal(len(z)).ln())
