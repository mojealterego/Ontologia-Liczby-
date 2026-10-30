"""Odtwarzalne kontrole arytmetyczne dla uzupełnień F10.1 i F10.2.
Testy liczbowe nie są formalnym dowodem twierdzeń w manuskrypcie.
Uruchomienie: python -m unittest discover -s tests -p test_f10.py -v
"""
import math
import unittest
from fractions import Fraction
from itertools import product


def digits(n: int, base: int) -> list[int]:
    if base < 2 or n < 0:
        raise ValueError("expected base>=2 and n>=0")
    result = []
    while n:
        n, digit = divmod(n, base)
        result.append(digit)
    return result[::-1] or [0]


def horner(ds: list[int], base: int) -> int:
    if base < 2 or not ds or any(not 0 <= d < base for d in ds):
        raise ValueError("invalid digits")
    value = 0
    for digit in ds:
        value = base * value + digit
    return value


def add_columns(a: int, b: int, base: int, width: int) -> tuple[int, int]:
    if not (base >= 2 and width > 0 and 0 <= a < base**width and 0 <= b < base**width):
        raise ValueError("invalid input")
    carry = 0
    result = 0
    for k in range(width):
        total = (a // base**k) % base + (b // base**k) % base + carry
        carry, digit = divmod(total, base)
        result += digit * base**k
    return result, carry


def subtract_columns(a: int, b: int, base: int, width: int) -> tuple[int, int]:
    if not (base >= 2 and width > 0 and 0 <= a < base**width and 0 <= b < base**width):
        raise ValueError("invalid input")
    borrow = 0
    result = 0
    for k in range(width):
        difference = (a // base**k) % base - (b // base**k) % base - borrow
        borrow = int(difference < 0)
        result += (difference % base) * base**k
    return result, borrow


def terminating(frac: Fraction, base: int) -> bool:
    q = frac.denominator
    while q > 1:
        d = math.gcd(q, base)
        if d == 1:
            return False
        q //= d
    return True


class TestF101(unittest.TestCase):
    def test_01_roundtrip(self):
        for base in range(2, 37):
            for n in range(701):
                self.assertEqual(horner(digits(n, base), base), n)

    def test_02_length_integer_bounds(self):
        for base in (2,3,4,5,8,10,16,32):
            self.assertEqual(digits(0, base), [0])
            for n in range(1, 3000):
                ds = digits(n, base)
                self.assertGreater(ds[0], 0)
                self.assertLessEqual(base**(len(ds)-1), n)
                self.assertLess(n, base**len(ds))

    def test_03_leading_zero_equivalence(self):
        for base in range(2, 18):
            for n in range(100):
                self.assertEqual(horner([0,0,0]+digits(n,base),base),n)

    def test_04_all_fixed_width_words(self):
        for base, width in product(range(2,9),range(1,5)):
            vals = [horner(list(ds),base) for ds in product(range(base),repeat=width)]
            self.assertEqual(set(vals),set(range(base**width)))

    def test_05_explicit_examples(self):
        self.assertEqual(horner([5,7,2],8),378)
        self.assertEqual(digits(1024,2),[1]+[0]*10)
        self.assertEqual(7**4-7**3,2058)
        self.assertEqual(horner([7,14,10],16),2026)
        self.assertEqual(Fraction(2,36),Fraction(1,18))

    def test_06_terminating_fraction(self):
        self.assertTrue(terminating(Fraction(7,40),10))
        self.assertFalse(terminating(Fraction(7,40),2))
        self.assertTrue(terminating(Fraction(1,18),6))
        for base in range(2,17):
            for q in range(2,80):
                self.assertEqual(terminating(Fraction(1,q),base),
                                 any(base**k % q == 0 for k in range(30)))

    def test_07_fraction_truncation(self):
        for base in range(2,13):
            for q in range(2,25):
                for p in range(1,q):
                    f = Fraction(p,q)
                    for precision in (1,2,4,7):
                        value = f*base**precision
                        approx = Fraction(value.numerator//value.denominator,base**precision)
                        self.assertTrue(0 <= f-approx < Fraction(1,base**precision))

    def test_08_two_complement_range(self):
        for width in range(1,10):
            vals = [u if u < 2**(width-1) else u-2**width for u in range(2**width)]
            self.assertEqual(sorted(vals),list(range(-2**(width-1),2**(width-1))))

    def test_09_repeating_decimal(self):
        self.assertEqual(digits(255,2),[1]*8)
        self.assertEqual(digits(255,16),[15,15])
        remainder=1
        ds=[]
        for _ in range(6):
            digit,remainder=divmod(remainder*10,7)
            ds.append(digit)
        self.assertEqual(ds,[1,4,2,8,5,7])
        self.assertEqual(remainder,1)


class TestF102(unittest.TestCase):
    def test_10_exhaustive_addition(self):
        for base,width in ((2,5),(3,4),(5,3),(10,2)):
            for a in range(base**width):
                for b in range(base**width):
                    low,carry=add_columns(a,b,base,width)
                    self.assertEqual(low+carry*base**width,a+b)
                    self.assertIn(carry,(0,1))

    def test_11_exhaustive_subtraction(self):
        for base,width in ((2,5),(3,4),(10,2)):
            for a in range(base**width):
                for b in range(base**width):
                    low,borrow=subtract_columns(a,b,base,width)
                    self.assertEqual(low-borrow*base**width,a-b)
                    self.assertEqual(borrow,int(a<b))

    def test_12_multi_addend_carry(self):
        for base in (2,3,5,10):
            for count in range(1,9):
                width=3
                vals=[(base**width-1-7*i)%(base**width) for i in range(count)]
                carry=0
                low=0
                for k in range(width):
                    total=sum((v//base**k)%base for v in vals)+carry
                    carry,digit=divmod(total,base)
                    low+=digit*base**k
                self.assertEqual(low+carry*base**width,sum(vals))
                self.assertLessEqual(carry,count-1)

    def test_13_chapter_examples(self):
        self.assertEqual(horner([1,0,2,2],3),35)
        self.assertEqual(horner([2,1,1],3),22)
        self.assertEqual(digits(57,3),[2,0,1,0])
        self.assertEqual(add_columns(255,1,2,8),(0,1))
        self.assertEqual(subtract_columns(1000,1,10,4),(999,0))
        self.assertEqual(subtract_columns(16,1,2,5),(15,0))
        self.assertEqual(digits(35,3),[1,0,2,2])
        self.assertEqual(add_columns(230,40,2,8),(14,1))

    def test_14_boundary_carries(self):
        for base in (2,3,8,10,16):
            for width in (1,2,3):
                self.assertEqual(add_columns(base**width-1,1,base,width),(0,1))
                self.assertEqual(add_columns(0,0,base,width),(0,0))
                self.assertEqual(subtract_columns(0,0,base,width),(0,0))

    def test_15_exact_width_limit(self):
        self.assertEqual(subtract_columns(25,25,10,3),(0,0))
        self.assertEqual(add_columns(650,350,10,3),(0,1))
        self.assertEqual(add_columns(650,349,10,3),(999,0))

    def test_16_local_carry_examples(self):
        self.assertEqual(divmod(7+7+7+2,8),(2,7))
        self.assertEqual(divmod(9+9+1,10),(1,9))
        self.assertEqual(divmod(4+4+1,5),(1,4))


if __name__ == "__main__":
    unittest.main()
