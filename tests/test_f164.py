"""Finite verification of F16.4's base-B periods and exact rounding."""
from fractions import Fraction
from math import gcd
import unittest


def period_structure(a: int, b: int, base: int) -> tuple[int, int]:
    """Return exact (preperiod, period), with period=0 for terminating expansions."""
    if b <= 0 or base < 2 or gcd(abs(a), b) != 1:
        raise ValueError("canonical fraction and base >= 2 required")
    if a == 0:
        return 0, 0
    smooth, coprime = 1, b
    p = 2
    bb = base
    while p * p <= bb:
        if bb % p == 0:
            while bb % p == 0:
                bb //= p
            while coprime % p == 0:
                smooth *= p
                coprime //= p
        p += 1
    if bb > 1:
        while coprime % bb == 0:
            smooth *= bb
            coprime //= bb
    t, power = 0, 1
    while power % smooth != 0:
        power *= base
        t += 1
    if coprime == 1:
        return t, 0
    order, residue = 1, base % coprime
    while residue != 1:
        residue = (residue * base) % coprime
        order += 1
    return t, order


def observed_period(a: int, b: int, base: int) -> tuple[int, int]:
    """Detect first repeated remainder, independent of factorization."""
    if b <= 0 or base < 2 or gcd(abs(a), b) != 1:
        raise ValueError("invalid inputs")
    r, seen, step = abs(a) % b, {}, 0
    while r and r not in seen:
        seen[r] = step
        r = (r * base) % b
        step += 1
    if r == 0:
        return step, 0
    return seen[r], step - seen[r]


def interval(x: Fraction, base: int, digits: int) -> tuple[Fraction, Fraction]:
    if base < 2 or digits < 0:
        raise ValueError("invalid base or precision")
    scale = base ** digits
    numerator = x.numerator * scale
    denominator = x.denominator
    lo = numerator // denominator
    hi = -(-numerator // denominator)
    return Fraction(lo, scale), Fraction(hi, scale)


def nearest_even(x: Fraction, base: int, digits: int) -> Fraction:
    if base < 2 or digits < 0:
        raise ValueError("invalid base or precision")
    scale = base ** digits
    numerator = x.numerator * scale
    denominator = x.denominator
    q, r = divmod(numerator, denominator)
    if 2 * r > denominator or (2 * r == denominator and q % 2 != 0):
        q += 1
    return Fraction(q, scale)


class F164Tests(unittest.TestCase):
    def test_periods_exhaustive(self):
        for base in range(2, 17):
            for b in range(1, 121):
                for a in (1, b-1):
                    if gcd(abs(a), b) == 1:
                        self.assertEqual(period_structure(a, b, base), observed_period(a, b, base),
                                         (a, b, base))

    def test_examples(self):
        examples = [(1, 6, 10, (1, 1)), (1, 28, 10, (2, 6)),
                    (7, 40, 10, (3, 0)), (1, 12, 10, (2, 1)),
                    (1, 7, 10, (0, 6)), (1, 8, 2, (3, 0)),
                    (1, 10, 2, (1, 4)), (1, 3, 10, (0, 1))]
        for a, b, base, expected in examples:
            with self.subTest(a=a, b=b, base=base):
                self.assertEqual(period_structure(a, b, base), expected)

    def test_interval_bounds(self):
        for base in (2, 3, 10, 16):
            for digits in range(5):
                for b in range(1, 29):
                    for a in range(-30, 31):
                        x = Fraction(a, b)
                        lo, hi = interval(x, base, digits)
                        self.assertLessEqual(lo, x)
                        self.assertLessEqual(x, hi)
                        self.assertIn(hi - lo, (Fraction(0), Fraction(1, base ** digits)))

    def test_nearest_even_bound(self):
        for base in (2, 3, 10, 16):
            for digits in range(5):
                for b in range(1, 27):
                    for a in range(-27, 28):
                        x = Fraction(a, b)
                        rounded = nearest_even(x, base, digits)
                        self.assertLessEqual(abs(x-rounded), Fraction(1, 2*base**digits))
        self.assertEqual(nearest_even(Fraction(1, 8), 10, 2), Fraction(12, 100))
        self.assertEqual(nearest_even(Fraction(-1, 8), 10, 2), Fraction(-12, 100))

    def test_quotient_error_bound(self):
        for x in (Fraction(-3, 2), Fraction(0), Fraction(2, 3), Fraction(5)):
            for y in (Fraction(-4), Fraction(-1, 2), Fraction(1), Fraction(3)):
                for dx in (Fraction(-1, 10), Fraction(0), Fraction(1, 10)):
                    for dy in (Fraction(-1, 5), Fraction(0), Fraction(1, 5)):
                        ex, ey = Fraction(1, 10), Fraction(1, 5)
                        bound = (abs(y)*ex+abs(x)*ey)/(abs(y)*(abs(y)-ey))
                        actual = abs((x+dx)/(y+dy)-x/y)
                        self.assertLessEqual(actual, bound)

    def test_remainder_digit_certificate(self):
        for base in (2, 3, 10, 16):
            for b in range(1, 70):
                for a in (1, b-1):
                    if gcd(abs(a), b) != 1:
                        continue
                    remainder = abs(a) % b
                    for step in range(1, 20):
                        digit, remainder = divmod(base * remainder, b)
                        self.assertTrue(0 <= digit < base)
                        self.assertTrue(0 <= remainder < b)
                        self.assertEqual(remainder, (pow(base, step, b) * abs(a)) % b)

    def test_cancellation_condition_bound(self):
        for x in (Fraction(-5, 2), Fraction(0), Fraction(1), Fraction(1001, 1000)):
            for y in (Fraction(-1), Fraction(0), Fraction(1), Fraction(3, 2)):
                if x == y:
                    continue
                eps = Fraction(1, 100)
                for dx in (-eps*abs(x), Fraction(0), eps*abs(x)):
                    for dy in (-eps*abs(y), Fraction(0), eps*abs(y)):
                        actual = abs(dx-dy)/abs(x-y)
                        kappa = (abs(x)+abs(y))/abs(x-y)
                        self.assertLessEqual(actual, eps*kappa)

    def test_disjoint_interval_order(self):
        values = [Fraction(a, b) for b in range(1, 8) for a in range(-8, 9)]
        for base in (2, 10):
            for digits in (0, 1, 2):
                bounds = [(x, interval(x, base, digits)) for x in values]
                for x, (_, ux) in bounds:
                    for y, (ly, _) in bounds:
                        if ux < ly:
                            self.assertLess(x, y)

    def test_invalid(self):
        for a, b, base in ((1, 0, 10), (2, 4, 10), (1, 3, 1)):
            with self.assertRaises(ValueError):
                period_structure(a, b, base)
        with self.assertRaises(ValueError):
            interval(Fraction(1, 3), 10, -1)


if __name__ == "__main__":
    unittest.main()
