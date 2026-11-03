import unittest
from fractions import Fraction as F

def budget(qs, ds, initial):
    x=initial
    for q,d in zip(qs,ds):
        assert F(0)<=q<F(1) and d>=0
        x=q*x+d
    return x

class VariableContractions(unittest.TestCase):
    def test_z1_z2(self):
        self.assertEqual(budget([F(1,2)],[F(1,4)],F(4)),F(9,4))
        self.assertEqual(budget([F(1,2),F(1,4)],[F(1,4),F(1,8)],F(4)),F(11,16))
    def test_z3(self):
        for n in range(1,20):
            self.assertEqual(budget([F(1,2)]*n,[F(0)]*n,F(8)),F(8,2**n))
    def test_z4_resonance(self):
        for n in range(1,20):
            self.assertEqual(budget([F(1,2)]*n,[F(1,2**(k+1)) for k in range(n)],F(0)),F(n,2**n))
    def test_z6(self):
        for n in range(1,20):
            self.assertEqual(budget([F(1,2)]*n,[F(1,4)]*n,F(0)),F(1,2)*(1-F(1,2**n)))
    def test_z7_telescoping(self):
        for n in range(1,20):
            qs=[1-F(1,k+2) for k in range(n)]
            self.assertEqual(budget(qs,[F(0)]*n,F(1)),F(1,n+1))
    def test_sharpness(self):
        for n in range(1,15):
            qs=[F(k+1,k+3) for k in range(n)]
            ds=[F(1,k+5) for k in range(n)]
            exact=F(3)
            for q,d in zip(qs,ds): exact=q*exact+d
            self.assertEqual(exact,budget(qs,ds,F(3)))
    def test_residual(self):
        self.assertEqual((F(1,8)+F(1,8))/(1-F(1,2)),F(1,2))

if __name__=='__main__': unittest.main()
