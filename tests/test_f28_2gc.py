"""Regression checks for F28.2-GC; run: python -m unittest tests/test_f28_2gc.py -v."""
import math
import unittest
from fractions import Fraction

class QuadratureGC(unittest.TestCase):
    def test_constant_exact(self):
        for n in range(1, 101):
            q = sum((Fraction(k, n) for k in range(n)), Fraction()) / n
            self.assertEqual(Fraction(1, 2) - q, Fraction(1, 2*n))

    def test_adaptive_bound(self):
        for n in range(1, 101):
            for l in (0, 1, 2, 5):
                exact = Fraction(1, 2*n) + Fraction(l*(n-1), 4*n*n)
                sumform = Fraction(1, 2*n) + Fraction(l, 2*n**3)*sum(range(n))
                self.assertEqual(exact, sumform)
                self.assertLessEqual(exact, Fraction(1, 2*n)+Fraction(l, 4*n))

    def test_linear_phase(self):
        for n in (2, 4, 8, 16, 32, 64):
            phase = lambda t: 0.7*t
            q = sum((k/n)*math.cos(phase(k/n)) for k in range(n))/n
            a = math.sin(0.7)/0.7+(math.cos(0.7)-1)/(0.7**2)
            bound = 1/(2*n)+0.7*(n-1)/(4*n*n)
            self.assertLessEqual(abs(a-q), bound+1e-12)

    def test_aliasing(self):
        for n in (2, 3, 7, 10):
            q = sum((k/n)*math.cos(2*math.pi*k) for k in range(n))/n
            self.assertAlmostEqual(q, (n-1)/(2*n), places=12)

if __name__ == "__main__":
    unittest.main()
