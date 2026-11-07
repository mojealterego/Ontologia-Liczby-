"""Regresja F28.2-FZ: dokładna teleskopowa reprezentacja i granice profilu."""
import math
import unittest
from fractions import Fraction

class FZTests(unittest.TestCase):
    def test_telescope_exact(self):
        for n in range(1, 45):
            x = Fraction(3, 7)
            for k in range(n):
                x = Fraction(k + 1, k + 2) * x + Fraction((-1)**k, 1)
            closed = (Fraction(3, 7) + sum((k + 2) * (-1)**k for k in range(n))) / (n + 1)
            self.assertEqual(x, closed)

    def test_constant_phase(self):
        for n in (10, 100, 1000):
            x = 0.0
            for k in range(n):
                x = (k + 1) / (k + 2) * x + 1.0
            self.assertLess(abs(x / n - 0.5), 2 / n)

    def test_lipschitz_phase(self):
        for lam in (-3.0, -1.0, 0.0, 2.0, 5.0):
            n = 2000
            x = 0.0
            for k in range(n):
                x = (k + 1) / (k + 2) * x + math.cos(lam * k / n)
            target = 0.5 if lam == 0 else math.sin(lam)/lam + (math.cos(lam)-1)/(lam*lam)
            self.assertLess(abs(x/n - target), (abs(lam)+12)/n)

if __name__ == "__main__":
    unittest.main()
