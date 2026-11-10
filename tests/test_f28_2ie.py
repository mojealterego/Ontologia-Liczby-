"""Exact rational regression tests for F28.2-IE."""
from fractions import Fraction as F
import unittest

def bounds(rows):
    low = F(0)
    high = F(0)
    for alpha, beta, ell, upper in rows:
        assert 0 <= alpha <= beta and 0 <= ell <= upper and upper > 0
        low = max(low, alpha / upper)
        b = (beta / ell if ell else (float("inf") if beta else F(0)))
        high = max(high, b)
    return low, high

class IntervalCertificateTests(unittest.TestCase):
    def test_exact_grid(self):
        n = 0
        for a in range(5):
            for g in range(1, 8):
                for delta in range(4):
                    for eta in range(4):
                        actual_a, actual_g = F(a), F(g)
                        lo, hi = bounds([(max(F(0),actual_a-delta),actual_a+delta,
                                          max(F(0),actual_g-eta),actual_g+eta)])
                        self.assertLessEqual(lo, actual_a/actual_g)
                        self.assertLessEqual(actual_a/actual_g, hi)
                        n += 1
        self.assertEqual(n, 560)

    def test_zero_numerator(self):
        self.assertEqual(bounds([(F(0),F(0),F(0),F(5))]),(F(0),F(0)))

    def test_zero_gap_bound(self):
        self.assertEqual(bounds([(F(0),F(1),F(0),F(2))])[1],float("inf"))

    def test_two_directions(self):
        self.assertEqual(bounds([(F(1),F(2),F(2),F(4)),
                                 (F(3),F(4),F(4),F(8))]),(F(3,8),F(1)))

    def test_monotonic_refinement(self):
        old = bounds([(F(0),F(4),F(0),F(8))])
        new = bounds([(F(1),F(3),F(2),F(6))])
        self.assertLessEqual(old[0],new[0])
        self.assertGreaterEqual(old[1],new[1])

if __name__ == "__main__":
    unittest.main()
