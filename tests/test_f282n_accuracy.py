import unittest
from fractions import Fraction as F

def budget(q, errors):
    b = F(0)
    for e in errors:
        b = q*b+e
    return b

class VariableAccuracy(unittest.TestCase):
    def test_recurrence(self):
        self.assertEqual(budget(F(1,2),[F(1,4),F(1,8)]),F(1,4))
    def test_distinct_rates(self):
        for q,s in [(F(1,2),F(1,4)),(F(1,4),F(1,2)),(F(0),F(1,2))]:
            for n in range(1,12):
                errors=[s**j for j in range(n)]
                self.assertEqual(budget(q,errors),(q**n-s**n)/(q-s))
    def test_resonance(self):
        for q in [F(0),F(1,4),F(1,2),F(3,4)]:
            for n in range(1,10):
                self.assertEqual(budget(q,[q**j for j in range(n)]),n*q**(n-1))
    def test_sharpness(self):
        for q in [F(0),F(1,4),F(1,2)]:
            x=F(4); errors=[F(1,2)**j for j in range(8)]
            for n,e in enumerate(errors,1):
                x=q*x+e
                self.assertEqual(x,q**n*4+budget(q,errors[:n]))
    def test_exercises(self):
        self.assertEqual(F(1,2)*4+F(1,4),F(9,4))
        self.assertEqual(F(1,2)**2*4+budget(F(1,2),[F(1,4),F(1,8)]),F(5,4))
        self.assertEqual(budget(F(1,2),[F(1),F(1,4)]),F(3,4))
        self.assertEqual(budget(F(1,2),[F(1),F(1,2),F(1,4)]),F(3,4))
        self.assertEqual(budget(F(1,4),[F(2),F(1,2)]),F(1))
    def test_residual_certificates(self):
        self.assertEqual((F(1,8)+F(1,8))/(1-F(1,2)),F(1,2))
        self.assertEqual(F(1,16)/(1-F(3,4)),F(1,4))

if __name__=='__main__': unittest.main()
