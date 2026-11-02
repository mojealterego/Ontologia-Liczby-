"""Tests for E1-03, standard library only."""
import math
import unittest
from fractions import Fraction

class PowersRoots(unittest.TestCase):
    def test_integer_exponents(self):
        for a in range(1, 12):
            for m in range(-5, 6):
                for n in range(-5, 6):
                    self.assertEqual(Fraction(a) ** m * Fraction(a) ** n, Fraction(a) ** (m+n))

    def test_square_root_absolute(self):
        for a in range(-100, 101):
            self.assertEqual(math.isqrt(a*a), abs(a))

    def test_simplified_roots(self):
        self.assertEqual(6*6*2, 72)
        self.assertEqual(5*5*2, 50)
        self.assertEqual(6*6*3, 108)

    def test_exact_rational_powers(self):
        self.assertEqual(27 ** (2/3), 9.0)
        self.assertEqual(16 ** (3/4), 8.0)

    def test_interval_certificates(self):
        self.assertLess(Fraction(141,100)**2, 2)
        self.assertGreater(Fraction(142,100)**2, 2)
        self.assertLess(Fraction(7)**2, 60)
        self.assertGreater(Fraction(8)**2, 60)

    def test_am_gm_square(self):
        for a in range(20):
            for b in range(20):
                self.assertGreaterEqual((a+b)**2, 4*a*b)

    def test_power_monotonicity(self):
        for n in range(1, 12):
            self.assertLess(Fraction(1,2)**(n+1), Fraction(1,2)**n)
            self.assertGreater(2**(n+1), 2**n)

    def test_divisibility(self):
        for n in range(1, 30):
            self.assertEqual((10**n-1)%9, 0)

if __name__ == "__main__":
    unittest.main()
