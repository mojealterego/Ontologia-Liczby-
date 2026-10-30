"""Odtwarzalne kontrole numeryczne F10.3 (bez walidacji tez historycznych)."""
from fractions import Fraction
from math import gcd
import unittest


def encode60(n):
    if n < 0:
        raise ValueError
    ds = []
    while n:
        n, r = divmod(n, 60)
        ds.append(r)
    return ds[::-1] or [0]


def decode60(ds):
    assert ds and all(0 <= d < 60 for d in ds)
    n = 0
    for d in ds:
        n = 60*n + d
    return n


def terminates60(fr):
    q = fr.denominator
    while q > 1:
        g = gcd(q, 60)
        if g == 1:
            return False
        q //= g
    return True


class TestF103(unittest.TestCase):
    def test_01_conversion_round_trip(self):
        for n in range(10001):
            self.assertEqual(decode60(encode60(n)), n)

    def test_02_placeholder_changes_value(self):
        self.assertEqual(decode60([1,0,1]), 3601)
        self.assertEqual(decode60([1,1]), 61)
        self.assertEqual(decode60([1,0,1])-decode60([1,1]), 3540)

    def test_03_horner_examples(self):
        self.assertEqual(decode60([3,12,8]), 11528)
        self.assertEqual(decode60([4,5,6]), 14706)
        self.assertEqual(encode60(3661), [1,1,1])

    def test_04_terminating_fractions(self):
        for q in (2,3,5,8,12,18,25,120,125,216,1000,1800):
            self.assertTrue(terminates60(Fraction(1,q)))
            m = 0
            while 60**m % q:
                m += 1
            if m:
                self.assertNotEqual(60**(m-1) % q, 0)
        self.assertFalse(terminates60(Fraction(1,14)))
        self.assertFalse(terminates60(Fraction(1,7)))
        self.assertEqual(Fraction(30,3600), Fraction(1,120))
        self.assertEqual(Fraction(5,60), Fraction(1,12))

    def test_05_seven_period(self):
        remainder=1
        ds=[]
        rs=[]
        for _ in range(3):
            d,remainder=divmod(remainder*60,7)
            ds.append(d);rs.append(remainder)
        self.assertEqual(ds,[8,34,17])
        self.assertEqual(rs,[4,2,1])

    def test_06_fractions_and_truncation(self):
        self.assertEqual(Fraction(7,60)+Fraction(30,3600),Fraction(1,8))
        for q in range(2,81):
            value=Fraction(1,q)
            rem=value
            approximant=Fraction(0)
            for n in range(1,6):
                digit=int(rem*60)
                rem=rem*60-digit
                approximant+=Fraction(digit,60**n)
                self.assertTrue(0 <= value-approximant < Fraction(1,60**n))

    def test_07_time_carry(self):
        a=2*3600+48*60+55
        b=1*3600+23*60+15
        self.assertEqual(a+b,4*3600+12*60+10)
        self.assertEqual(3600+59*60+50+20,2*3600+10)

    def test_08_carry_and_units(self):
        for a in range(1,120):
            for b in range(1,120):
                self.assertEqual(decode60(encode60(a+b)),a+b)
        self.assertEqual(Fraction(30,60),Fraction(1,2))
        self.assertNotEqual(Fraction(30,60),Fraction(30,100))


if __name__=="__main__":
    unittest.main()
