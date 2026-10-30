"""Kontrole skończonych przykładów F14.3; nie zastępują dowodów ogólnych."""
from fractions import Fraction
from itertools import product
from math import floor, gcd, isqrt
from pathlib import Path
import re
import unittest

MANUSCRIPT = Path(__file__).resolve().parents[1] / "F14.3_UZUPELNIENIE_KONSTRUKCJA_WYMIERNYCH.md"


class TestF143(unittest.TestCase):
    def test_document_sections(self):
        text = MANUSCRIPT.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"\*\*Twierdzenie T\d+", text)), 12)
        self.assertEqual(len(re.findall(r"\*\*Zadanie \d+", text)), 12)
        self.assertEqual(len(re.findall(r"\*\*Kontrprzykład K\d+", text)), 6)
        self.assertGreater(len(text), 12000)

    def test_equivalence_transitivity_sample(self):
        for a, b, n, m in product(range(-3, 4), [1, 2, 3, -1, -2], [1, 2, -1], [1, 2, -1]):
            c, d = a*n, b*n
            e, f = c*m, d*m
            self.assertEqual(a*d, b*c)
            self.assertEqual(c*f, d*e)
            self.assertEqual(a*f, b*e)

    def test_well_defined_addition_and_product(self):
        for a, b, c, d in product(range(-3, 4), [1, 2, -1], range(-3, 4), [1, 3, -2]):
            self.assertEqual(Fraction(a*2, b*2) + Fraction(c*-3, d*-3), Fraction(a*d+b*c, b*d))
            self.assertEqual(Fraction(a*2, b*2) * Fraction(c*-3, d*-3), Fraction(a*c, b*d))

    def test_canonical_sign(self):
        for a in range(-18, 19):
            for b in range(-9, 10):
                if b:
                    q = Fraction(a, b)
                    self.assertGreater(q.denominator, 0)
                    self.assertEqual(gcd(abs(q.numerator), q.denominator), 1)
                    self.assertEqual(Fraction(q.numerator, q.denominator), q)

    def test_order_cross_products(self):
        for a, b, c, d in product(range(-5, 6), range(1, 5), range(-5, 6), range(1, 5)):
            self.assertEqual(Fraction(a, b) < Fraction(c, d), a*d < b*c)

    def test_negative_floor(self):
        for a in range(-50, 51):
            for b in range(1, 14):
                q, r = divmod(a, b)
                self.assertEqual(Fraction(a, b), q + Fraction(r, b))
                self.assertEqual(q, floor(Fraction(a, b)))
                self.assertLess(r, b)
                self.assertGreaterEqual(r, 0)

    def test_mediant_between(self):
        for a, b, c, d in product(range(-4, 5), range(1, 9), range(-4, 5), range(1, 9)):
            if a*d < b*c:
                middle = Fraction(a+c, b+d)
                self.assertLess(Fraction(a, b), middle)
                self.assertLess(middle, Fraction(c, d))
                if b*c-a*d == 1:
                    self.assertEqual(gcd(abs(a+c), b+d), 1)

    def test_bounded_denominator_gap(self):
        for N in range(1, 9):
            seq = sorted({Fraction(a, b) for b in range(1, N+1) for a in range(-N, N+1)})
            for x, y in zip(seq, seq[1:]):
                self.assertGreaterEqual(y-x, Fraction(1, N*N))

    def test_density_constructive_small(self):
        for x, y in product([Fraction(i, 7) for i in range(-3, 4)], repeat=2):
            if x < y:
                n = (y-x).denominator*2
                self.assertGreater(n*(y-x), 1)
                m = (x*n).numerator // (x*n).denominator + 1
                self.assertLess(x, Fraction(m, n))
                self.assertLess(Fraction(m, n), y)

    def test_rational_grid(self):
        for a, b, n in product(range(-25, 26), range(1, 12), range(1, 13)):
            x = Fraction(a, b)
            q = Fraction((x*n).numerator // (x*n).denominator, n)
            self.assertLessEqual(0, x-q)
            self.assertLess(x-q, Fraction(1, n))
            if n % x.denominator == 0:
                self.assertEqual(x, q)

    def test_exercise_values(self):
        self.assertEqual(Fraction(15, -21), Fraction(-5, 7))
        self.assertEqual(Fraction(5, 12) + Fraction(7, 18), Fraction(29, 36))
        self.assertEqual(Fraction(-21, 10) * Fraction(-10, 21), 1)
        self.assertEqual(Fraction(-462, -1078), Fraction(3, 7))
        self.assertLess(Fraction(-7, 11), Fraction(-5, 8))
        self.assertEqual(Fraction(-29, 6), -5 + Fraction(1, 6))
        self.assertGreater(Fraction(3, 2)**2, 2)
        self.assertLess(Fraction(3, 2)**2, 3)
        self.assertEqual(Fraction(1+2, 3+5), Fraction(3, 8))
        self.assertLess(Fraction(1, 200), Fraction(1, 100))
        self.assertEqual(Fraction(7, 6) - Fraction(1, 1), Fraction(1, 6))
        self.assertEqual(Fraction(9,14) * Fraction(-2, 3), Fraction(-3, 7))

    def test_no_unqualified_division(self):
        content = MANUSCRIPT.read_text(encoding="utf-8")
        self.assertIn('mianowniki są niezerowe', content)
        self.assertIn('charakterystyki zero', content)


if __name__ == "__main__":
    unittest.main()