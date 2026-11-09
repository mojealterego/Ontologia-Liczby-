import unittest
from fractions import Fraction as F

def radius_squared(c, q):
    """Squared exact robustness radius on a box at its origin; None means infinity."""
    vals = [F(ci * ci, qi) for ci, qi in zip(c, q) if qi > 0]
    return min(vals) if vals else None

class TestSingularEllipsoid(unittest.TestCase):
    def test_exact_grid(self):
        count = 0
        for a in range(1, 10):
            for b in range(1, 10):
                for q1 in range(5):
                    for q2 in range(5):
                        expected = min(([F(a*a, q1)] if q1 else []) +
                                       ([F(b*b, q2)] if q2 else []), default=None)
                        self.assertEqual(radius_squared((a,b), (q1,q2)), expected)
                        count += 1
        print("exact rational cases:", count)

    def test_invisible(self):
        self.assertEqual(radius_squared((3,5), (4,0)), F(9,4))
        self.assertIsNone(radius_squared((1,1), (0,0)))

    def test_monotonicity(self):
        for a in range(1,7):
            for q in range(1,7):
                self.assertGreaterEqual(radius_squared((a,), (q,)),
                                        radius_squared((a,), (q+1,)))

if __name__ == "__main__":
    unittest.main()
