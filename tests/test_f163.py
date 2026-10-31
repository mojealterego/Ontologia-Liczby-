"""Finite arithmetic checks for F16.3."""
from fractions import Fraction
from math import gcd
import unittest


def multiply(a, b, c, d):
    if b <= 0 or d <= 0:
        raise ValueError("positive denominators required")
    if gcd(abs(a), b) != 1 or gcd(abs(c), d) != 1:
        raise ValueError("canonical inputs required")
    g = gcd(abs(a), d)
    h = gcd(abs(c), b)
    return (a // g) * (c // h), (b // h) * (d // g)


def divide(a, b, c, d):
    if c == 0:
        raise ZeroDivisionError("division by zero")
    result = Fraction(a, b) / Fraction(c, d)
    return result.numerator, result.denominator


class F163Tests(unittest.TestCase):
    def test_multiplication_enumeration(self):
        for b in range(1, 10):
            for d in range(1, 10):
                for a in range(-10, 11):
                    if gcd(abs(a), b) != 1:
                        continue
                    for c in range(-10, 11):
                        if gcd(abs(c), d) != 1:
                            continue
                        p, q = multiply(a, b, c, d)
                        expected = Fraction(a, b) * Fraction(c, d)
                        self.assertEqual((p, q), (expected.numerator, expected.denominator))
                        self.assertEqual(gcd(abs(p), q), 1)
                        self.assertEqual((b*d) % q, 0)
                        self.assertLessEqual(max(abs(p), q), max(abs(a), b)*max(abs(c), d))

    def test_division_enumeration(self):
        for b in range(1, 8):
            for d in range(1, 8):
                for a in range(-8, 9):
                    if gcd(abs(a), b) != 1:
                        continue
                    for c in range(-8, 9):
                        if c == 0 or gcd(abs(c), d) != 1:
                            continue
                        p, q = divide(a, b, c, d)
                        self.assertEqual(Fraction(p, q), Fraction(a, b)/Fraction(c, d))
                        self.assertEqual(gcd(abs(p), q), 1)

    def test_examples(self):
        cases = [(2,3,3,5,(2,5)),(7,12,8,21,(2,9)),
                 (-5,14,7,15,(-1,6)),(0,1,17,23,(0,1)),
                 (3,10,5,9,(1,6)),(-2,5,-15,8,(3,4))]
        for a,b,c,d,expected in cases:
            self.assertEqual(multiply(a,b,c,d),expected)

    def test_division_examples(self):
        cases = [(4,9,2,3,(2,3)),(5,8,-15,16,(-2,3)),
                 (11,13,11,26,(2,1)),(13,17,26,51,(3,2))]
        for a,b,c,d,expected in cases:
            self.assertEqual(divide(a,b,c,d),expected)

    def test_zero_and_invalid(self):
        self.assertEqual(multiply(0,1,17,23),(0,1))
        with self.assertRaises(ZeroDivisionError):
            divide(1,2,0,1)
        with self.assertRaises(ValueError):
            multiply(2,4,1,3)


if __name__ == "__main__":
    unittest.main()
