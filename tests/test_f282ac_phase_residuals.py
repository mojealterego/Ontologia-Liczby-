import unittest
from fractions import Fraction as F

def bounds(L, a):
    m=len(L)
    if not m or len(a)!=m or any(x<0 for x in L+a):
        raise ValueError("nonnegative arrays of equal positive length required")
    Q=F(1)
    for x in L: Q*=x
    if Q>=1: raise ValueError("cycle not contractive")
    result=[]
    for i in range(m):
        B=F(0); weight=F(1)
        for k in range(m):
            B+=weight*a[(i-1-k)%m]
            weight*=L[(i-1-k)%m]
        result.append(B/(1-Q))
    return result

class PhaseResidualTests(unittest.TestCase):
    def test_two_phase(self):
        self.assertEqual(bounds([F(2),F(1,4)],[F(1,10),F(1,20)]),[F(3,20),F(2,5)])
    def test_single_phase(self):
        self.assertEqual(bounds([F(1,3)],[F(1,4)]),[F(3,8)])
    def test_zero_lipschitz(self):
        self.assertEqual(bounds([F(0),F(7)],[F(2),F(3)]),[F(17),F(2)])
    def test_invalid_cycle(self):
        with self.assertRaises(ValueError): bounds([F(2),F(1)],[F(1),F(1)])
    def test_parameterized_exact_sharpness(self):
        for p in range(1,6):
            for q in range(1,6):
                L=[F(p,3),F(1,2*p)]
                a=[F(q,17),F(1,13)]
                c=bounds(L,a)
                self.assertEqual(c[1],L[0]*c[0]+a[0])
                self.assertEqual(c[0],L[1]*c[1]+a[1])
    def test_monotonicity(self):
        L=[F(2),F(1,4)]
        low=bounds(L,[F(1,10),F(1,20)])
        high=bounds(L,[F(1,5),F(1,10)])
        self.assertTrue(all(x<=y for x,y in zip(low,high)))

if __name__=="__main__": unittest.main()
