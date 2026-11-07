"""F28.2-FY: independent numerical and exact regression checks."""
import math
import unittest
from fractions import Fraction

def iterate(n, lam=0.0, eta=0.0, b=0.0):
    x = b
    for k in range(n):
        x = (k + 1) / (k + 2) * x + math.cos(k * lam / n + k * eta / (n * n))
    return x / n

def moments(lam, steps=20000):
    # Composite midpoint quadrature, second-order convergence.
    i = j = k = 0.0
    for a in range(steps):
        t = (a + 0.5) / steps
        i += t * math.cos(lam * t)
        j += math.cos(lam * t)
        k += t * t * math.sin(lam * t)
    return i / steps, j / steps, k / steps

class FYTests(unittest.TestCase):
    def test_exact_telescope(self):
        for n in range(1, 45):
            x = Fraction(7, 11)
            for k in range(n):
                x = Fraction(k + 1, k + 2) * x + 1
            closed = (Fraction(7, 11) + sum(range(2, n + 2))) / (n + 1)
            self.assertEqual(x, closed)

    def test_zero_phase_exact(self):
        for n in range(1, 80):
            self.assertAlmostEqual(iterate(n), (n + 3) / (2 * (n + 1)), places=12)

    def test_second_order(self):
        for lam, eta in [(0.0, 0.0), (1.3, 0.7), (2.0, -1.1), (3.14, 2.5)]:
            i, j, k = moments(lam)
            bcoef = -math.cos(lam) / 2 + 2 * j - eta * k - i
            for n in (250, 500, 1000):
                error = abs(iterate(n, lam, eta, 0.25) - i - bcoef / n)
                self.assertLess(error * n * n, 15.0)

if __name__ == "__main__":
    unittest.main()
