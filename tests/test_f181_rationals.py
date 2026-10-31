"""Finite exact-arithmetic checks for F18.1; not formal verification."""
from __future__ import annotations

import math
import re
import unittest
from fractions import Fraction
from pathlib import Path


def height(q: Fraction) -> int:
    return max(abs(q.numerator), q.denominator)


def digits(q: Fraction, base: int, count: int):
    assert 0 <= q < 1 and base >= 2
    rem = q.numerator
    den = q.denominator
    result = []
    for _ in range(count):
        digit, rem = divmod(base * rem, den)
        result.append(digit)
    return result, rem


class F181ExactChecks(unittest.TestCase):
    def test_01_normalization(self):
        self.assertEqual(Fraction(-84, -126), Fraction(2, 3))
        self.assertEqual(Fraction(0, -51), Fraction(0, 1))
        for a in range(-30, 31):
            for b in range(1, 31):
                q = Fraction(a, b)
                self.assertEqual(math.gcd(abs(q.numerator), q.denominator), 1)
                self.assertGreater(q.denominator, 0)

    def test_02_integer_multiples(self):
        for a in range(-12, 13):
            for b in range(1, 15):
                q = Fraction(a, b)
                for n in range(-20, 21):
                    self.assertEqual((n * q).denominator == 1, n % q.denominator == 0)

    def test_03_height_bounds(self):
        values = [Fraction(a, b) for a in range(-9, 10) for b in range(1, 10)]
        for x in values:
            for y in values:
                self.assertLessEqual(height(x*y), height(x)*height(y))
                self.assertLessEqual(height(x+y), 2*height(x)*height(y))

    def test_04_height_finite(self):
        for m in range(1, 8):
            qs = {Fraction(a, b) for a in range(-m, m+1) for b in range(1, m+1)
                  if max(abs(Fraction(a,b).numerator), Fraction(a,b).denominator) <= m}
            self.assertLessEqual(len(qs), m*(2*m+1))

    def test_05_mediants(self):
        values = sorted({Fraction(a, b) for a in range(-5, 6) for b in range(1, 7)})
        for x in values:
            for y in values:
                if x < y:
                    med = Fraction(x.numerator+y.numerator, x.denominator+y.denominator)
                    self.assertLess(x, med)
                    self.assertLess(med, y)

    def test_06_unimodular_barrier(self):
        vals = sorted({Fraction(a,b) for a in range(0, 10) for b in range(1, 10)})
        for x in vals:
            for y in vals:
                if x < y and x.denominator*y.numerator-x.numerator*y.denominator == 1:
                    med_num = x.numerator+y.numerator
                    med_den = x.denominator+y.denominator
                    self.assertEqual(math.gcd(med_num, med_den), 1)
                    for z in vals:
                        if x < z < y:
                            self.assertGreaterEqual(z.denominator, med_den)

    def test_07_decimal_remainders(self):
        for b in range(2, 40):
            for a in range(1, b):
                q = Fraction(a, b)
                ds, rem = digits(q, 10, 30)
                numerator = sum(d * 10**(29-i) for i, d in enumerate(ds))
                self.assertEqual(q, Fraction(numerator, 10**30)+Fraction(rem, q.denominator*10**30))

    def test_08_terminating_criterion(self):
        for base in range(2, 13):
            for b in range(2, 45):
                q = Fraction(1, b)
                d, rem = digits(q, base, 20)
                divides_power = any(pow(base,k,b)==0 for k in range(0, 21))
                self.assertEqual(rem==0, divides_power)

    def test_09_period_order(self):
        for base in range(2, 11):
            for b in range(2, 30):
                if math.gcd(base,b) != 1:
                    continue
                period = next(k for k in range(1, 100) if pow(base,k,b)==1)
                for a in range(1, b):
                    if math.gcd(a,b) != 1:
                        continue
                    ds, rem = digits(Fraction(a,b), base, 2*period)
                    self.assertEqual(ds[:period], ds[period:])
                    self.assertEqual(rem, a)

    def test_10_repeating_decimal_examples(self):
        self.assertEqual(digits(Fraction(1,7),10,6)[0], [1,4,2,8,5,7])
        self.assertEqual(digits(Fraction(7,40),10,3)[0], [1,7,5])
        self.assertEqual(digits(Fraction(1,12),10,5)[0], [0,8,3,3,3])
        self.assertEqual(Fraction(27,99), Fraction(3,11))

    def test_11_mediant_representative_dependence(self):
        self.assertNotEqual(Fraction(1+1,2+3), Fraction(2+1,4+3))

    def test_12_document_numbering(self):
        base = Path(__file__).resolve().parent
        candidates = [
            base / 'F18.1_UZUPELNIENIE_STRUKTURALNE_Q.md',
            base.parent / 'manuscript' / 'tom-01' / 'F18' / 'F18.1_UZUPELNIENIE_STRUKTURALNE_Q.md',
        ]
        p = next((candidate for candidate in candidates if candidate.is_file()), None)
        self.assertIsNotNone(p, 'F18.1 source file must exist')
        source = p.read_text(encoding='utf-8')
        for marker, end in [('D',8),('T',12),('K',6),('Z',12)]:
            nums = [int(x) for x in re.findall(r'\*\*'+marker+r'(\d+)\b', source)]
            self.assertEqual(nums, list(range(1,end+1)), (marker, nums))


if __name__ == '__main__':
    unittest.main()
