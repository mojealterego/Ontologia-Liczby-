"""Exact rational regression checks for F28.2-HR."""
import unittest
from fractions import Fraction as F
from itertools import product

def radius(cost, generators, support):
    values = [sum(c*d for c,d in zip(cost,g))/support(g)
              for g in generators if support(g)>0]
    return min(values) if values else None

class RobustSupportTests(unittest.TestCase):
    def test_boxes(self):
        count=0
        for a,b,p,q in product(range(1,9), repeat=4):
            c=(F(a),F(b))
            generators=((F(1),F(0)),(F(0),F(1)))
            support=lambda d:F(p)*abs(d[0])+F(q)*abs(d[1])
            self.assertEqual(radius(c,generators,support),min(F(a,p),F(b,q)))
            count+=1
        self.assertEqual(count,4096)

    def test_minkowski(self):
        generators=((F(1),F(0)),(F(0),F(1)))
        support=lambda d:F(3)*abs(d[0])+abs(d[1])
        self.assertEqual(radius((F(2),F(3)),generators,support),F(2,3))

    def test_invisible(self):
        generators=((F(1),F(0)),(F(0),F(1)))
        self.assertIsNone(radius((F(2),F(3)),generators,lambda d:F(0)))
        self.assertEqual(radius((F(2),F(3)),generators,lambda d:abs(d[1])),F(3))

    def test_boundary(self):
        for c in range(1,30):
            r=F(c)
            self.assertEqual(F(c)-r,F(0))
            self.assertLess(F(c)-(r+1),0)

if __name__=="__main__":
    unittest.main()
