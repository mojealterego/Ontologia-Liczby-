import unittest
from fractions import Fraction as F

def clamp(x, lo, hi):
    return min(hi,max(lo,x))

class ProjectionJ(unittest.TestCase):
    def test_intervals(self):
        self.assertEqual(clamp(F(3),F(0),F(1)),1)
        self.assertEqual(max(F(0),max(F(-1),F(2))),2)
    def test_exact_bound(self):
        self.assertEqual(F(10)**2/F(25),4)
    def test_summable_errors(self):
        self.assertEqual(sum((F(1,2)**k for k in range(1,31)),F(0)),1-F(1,2)**30)
    def test_pythagorean_projection(self):
        for x in range(-5,6):
            p=clamp(x,0,2)
            for z in range(3):
                self.assertLessEqual((p-z)**2+(x-p)**2,(x-z)**2)
    def test_nonexpansive_projection(self):
        for x in range(-5,6):
            for y in range(-5,6):
                self.assertLessEqual(abs(clamp(x,0,2)-clamp(y,0,2)),abs(x-y))
    def test_oscillating_perturbation(self):
        x=0
        states=[]
        for k in range(6):
            x+=(-1)**k
            states.append(x)
        self.assertEqual(states,[1,0,1,0,1,0])

if __name__=="__main__":
    unittest.main()
