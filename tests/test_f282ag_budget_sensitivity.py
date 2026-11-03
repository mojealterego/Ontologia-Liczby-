import unittest
from fractions import Fraction as F

def value(a,b,c,u,h):
    return F(b)-F(a)*min(F(u),F(h)/F(c))

class BudgetSensitivity(unittest.TestCase):
    def test_monotone(self):
        v=[value(2,5,3,4,h) for h in range(20)]
        self.assertTrue(all(x>=y for x,y in zip(v,v[1:])))
    def test_convex_slopes(self):
        v=[value(2,5,3,4,h) for h in range(20)]
        slopes=[y-x for x,y in zip(v,v[1:])]
        self.assertTrue(all(x<=y for x,y in zip(slopes,slopes[1:])))
    def test_saturation(self):
        self.assertEqual(value(2,5,3,4,12),value(2,5,3,4,100))
    def test_lipschitz(self):
        for h in range(20):
            self.assertLessEqual(value(2,5,3,4,h)-value(2,5,3,4,h+1),F(2,3))
    def test_kink(self):
        self.assertEqual(value(1,1,1,1,0),1)
        self.assertEqual(value(1,1,1,1,1),0)
        self.assertEqual(value(1,1,1,1,2),0)

if __name__=="__main__":
    unittest.main()
