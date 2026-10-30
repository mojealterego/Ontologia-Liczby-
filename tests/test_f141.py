"""Executable finite-model checks for the F14.1 manuscript supplement."""
import importlib.util
import itertools
import math
import random
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "tools" / "long_divide.py"
spec = importlib.util.spec_from_file_location("long_divide", MODULE)
assert spec and spec.loader
import sys
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def digits_of(n, base):
    if n == 0:
        return (0,)
    digits = []
    while n:
        n, r = divmod(n, base)
        digits.append(r)
    return tuple(reversed(digits))


class TestLongDivision(unittest.TestCase):
    def test_all_small_dividends_and_divisors(self):
        for base in (2, 3, 7, 10, 16):
            for d in range(1, 31):
                for a in range(250):
                    cert = module.divide_digits(digits_of(a, base), base, d)
                    self.assertTrue(cert.verify())
                    self.assertEqual((cert.quotient, cert.remainder), divmod(a, d))

    def test_leading_zeros_and_empty(self):
        for base in (2, 10, 16):
            for a in range(60):
                c = module.divide_digits((0, 0) + digits_of(a, base), base, 11)
                self.assertEqual((c.quotient, c.remainder), divmod(a, 11))
        self.assertEqual((module.divide_digits((), 10, 7).quotient, module.divide_digits((), 10, 7).remainder), (0, 0))

    def test_corrupt_certificate_rejected(self):
        from dataclasses import replace
        cert = module.divide_digits((1, 0, 0, 2), 10, 7)
        self.assertFalse(replace(cert, remainders=(0, 1, 3, 2, 2)).verify())
        self.assertFalse(replace(cert, quotient_digits=(0, 1, 4, 4)).verify())
        self.assertFalse(replace(cert, digits=(1, 10, 0, 2)).verify())

    def test_signed_division(self):
        for a in range(-200, 201):
            for b in range(-30, 31):
                if b == 0:
                    continue
                q, r = module.euclidean_signed(a, b)
                self.assertEqual(a, b*q + r)
                self.assertTrue(0 <= r < abs(b))

    def test_concatenation(self):
        for base in (2, 10, 16):
            for x in range(30):
                for y in range(30):
                    for d in (2, 3, 7, 11):
                        m = len(digits_of(y, base))
                        a = x*base**m+y
                        self.assertEqual(a % d, (base**m*(x%d)+y)%d)

    def test_suffix(self):
        for n in range(10000):
            self.assertEqual(n % 8, (n % 1000) % 8)

    def test_single_digit_error(self):
        for base in (2, 10):
            for pos in range(4):
                for delta in range(-base+1, base):
                    if delta:
                        detected = (delta * base**pos) % 11 != 0
                        self.assertTrue(detected)
        self.assertEqual((9 * 10**3) % 9, 0)

    def test_fractional_examples(self):
        self.assertEqual(module.fractional_expansion(1, 8), ((1, 2, 5), 3, 0))
        self.assertEqual(module.fractional_expansion(1, 7), ((1, 4, 2, 8, 5, 7), 0, 6))
        self.assertEqual(module.fractional_expansion(1, 6), ((1, 6), 1, 1))
        self.assertEqual(module.fractional_expansion(0, 7), ((), 0, 0))

    def test_fractional_invariant(self):
        for base in (2, 3, 10):
            for d in range(2, 60):
                for r0 in range(d):
                    digits, pre, period = module.fractional_expansion(r0, d, base)
                    r = r0
                    for digit in digits:
                        q, r = divmod(base*r, d)
                        self.assertEqual(digit, q)
                    self.assertTrue(period > 0 or r == 0)
                    self.assertLessEqual(len(digits), d)
                    if period:
                        self.assertEqual(r, (pow(base, pre, d) * r0) % d)

    def test_terminating_criterion(self):
        for base in (2, 3, 10):
            for d in range(2, 40):
                for r0 in range(1, d):
                    digits, _, period = module.fractional_expansion(r0, d, base)
                    g = math.gcd(r0, d)
                    predicted = any(base**k % (d//g) == 0 for k in range(15))
                    self.assertEqual(period == 0, predicted)

    def test_invalid_inputs(self):
        for args in [((1,), 1, 3), ((10,), 10, 3), ((1,), 10, 0), ((True,), 10, 3)]:
            with self.assertRaises(ValueError):
                module.divide_digits(*args)
        for a,b in [(1,0),(1,1.0),(True,3)]:
            with self.assertRaises(ValueError):
                module.euclidean_signed(a,b)

    def test_tasks(self):
        c=module.divide_digits((1,3,7),10,12)
        self.assertEqual((c.quotient,c.remainder),(11,5))
        c=module.divide_digits((1,0,0,2),10,7)
        self.assertEqual((c.quotient,c.remainder),(143,1))
        self.assertEqual(module.euclidean_signed(-37,-5),(8,3))
        self.assertEqual((123456 % 8),0)
        self.assertEqual(12345 % 7,4)
        self.assertEqual((2**20+1)%3,2)


if __name__ == "__main__":
    unittest.main()