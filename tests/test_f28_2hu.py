import unittest
from fractions import Fraction as F

def radius(c, scenarios):
    exposures = [max(-k for k in scenarios)]
    return None if exposures[0] == 0 else F(c, exposures[0])

class NonconvexUncertainty(unittest.TestCase):
    def test_grid(self):
        for c in range(1, 31):
            for a in range(1, 31):
                k = [0, -a, -2*a]
                r = radius(c, k)
                self.assertEqual(r, F(c, 2*a))
                self.assertEqual(r, radius(c, [0, -2*a]))
                self.assertEqual(r, radius(c, list(reversed(k))))
                self.assertEqual(radius(c, [2*x for x in k]), r/2)
                self.assertEqual(c + r*(-2*a), 0)
                self.assertGreater(c + (r-F(1,10000))*(-2*a), 0)
                self.assertLess(c + (r+F(1,10000))*(-2*a), 0)

    def test_invisible(self):
        self.assertIsNone(radius(1, [0, 2, 5]))

    def test_asymmetric_orientation(self):
        self.assertEqual(radius(1, [0, -2]), F(1,2))
        self.assertIsNone(radius(1, [0, 2]))

    def test_union(self):
        for c in range(1, 30):
            for a in range(1, 20):
                for b in range(1, 10):
                    lhs=radius(c,[0,-a,-b])
                    self.assertEqual(lhs,min(radius(c,[0,-a]),radius(c,[0,-b])))

if __name__ == "__main__":
    unittest.main()
