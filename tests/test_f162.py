"""Finite regression for the exact F16.2 rational addition algorithm."""
from fractions import Fraction
from math import gcd, lcm
import unittest


def add(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    if b <= 0 or d <= 0:
        raise ValueError("denominators must be positive")
    if gcd(abs(a), b) != 1 or gcd(abs(c), d) != 1:
        raise ValueError("inputs must be canonical")
    g = gcd(b, d)
    numerator = a * (d // g) + c * (b // g)
    denominator = b * (d // g)
    h = gcd(abs(numerator), denominator)
    return numerator // h, denominator // h


class F162Tests(unittest.TestCase):
    def test_exhaustive_sums_and_subtractions(self):
        for b in range(1, 13):
            for d in range(1, 13):
                for a in range(-12, 13):
                    if gcd(abs(a), b) != 1:
                        continue
                    for c in range(-12, 13):
                        if gcd(abs(c), d) != 1:
                            continue
                        for sign in (1, -1):
                            p, q = add(a, b, sign * c, d)
                            expected = Fraction(a, b) + sign * Fraction(c, d)
                            self.assertEqual((p, q), (expected.numerator, expected.denominator))
                            self.assertEqual(gcd(abs(p), q), 1)
                            self.assertEqual(lcm(b, d) % q, 0)

    def test_examples(self):
        cases = [
            (1, 6, 1, 9, (5, 18)),
            (1, 6, 1, 3, (1, 2)),
            (7, 12, -5, 18, (11, 36)),
            (-3, 10, 1, 15, (-7, 30)),
            (5, 8, 3, 8, (1, 1)),
            (4, 7, -4, 7, (0, 1)),
            (2, 5, 3, 7, (29, 35)),
            (11, 30, 7, 45, (47, 90)),
            (-1, 4, -3, 10, (-11, 20)),
            (9, 14, 5, 21, (37, 42)),
            (13, 24, -1, 16, (23, 48)),
        ]
        for a, b, c, d, expected in cases:
            with self.subTest(a=a, b=b, c=c, d=d):
                self.assertEqual(add(a, b, c, d), expected)

    def test_height_bound(self):
        for b in range(1, 9):
            for d in range(1, 9):
                for a in range(-8, 9):
                    if gcd(abs(a), b) != 1:
                        continue
                    for c in range(-8, 9):
                        if gcd(abs(c), d) != 1:
                            continue
                        p, q = add(a, b, c, d)
                        self.assertLessEqual(max(abs(p), q), 2 * max(abs(a), b) * max(abs(c), d))

    def test_symmetry(self):
        for a, b, c, d in [(2, 5, 3, 7), (-3, 10, 1, 15), (0, 1, 1, 6)]:
            self.assertEqual(add(a, b, c, d), add(c, d, a, b))

    def test_input_validation(self):
        for args in [(1, 0, 1, 2), (1, -2, 1, 3), (2, 4, 1, 3)]:
            with self.assertRaises(ValueError):
                add(*args)


if __name__ == "__main__":
    unittest.main()
