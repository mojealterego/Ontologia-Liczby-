import unittest
from fractions import Fraction as F

class Contractions(unittest.TestCase):
    def test_fixed_point(self):
        self.assertEqual(F(2)/(1-F(1,3)),3)
    def test_radius(self):
        self.assertEqual(F(1,4)/(1-F(1,2)),F(1,2))
    def test_residual(self):
        self.assertEqual(F(1,2)/(1-F(3,4)),2)
    def test_exact_recurrence(self):
        x=F(0)
        for n in range(1,15):
            x=x/2+1
            self.assertEqual(x,2*(1-F(1,2)**n))
    def test_operator_stability(self):
        self.assertEqual(F(1,4)/(1-F(1,2)),F(1,2))
    def test_sharp_bound(self):
        for n in range(1,15):
            x=F(4)*F(1,2)**n+F(1,4)*(1-F(1,2)**n)/(1-F(1,2))
            y=F(4)
            for _ in range(n):
                y=y/2+F(1,4)
            self.assertEqual(x,y)

if __name__=='__main__':
    unittest.main()
