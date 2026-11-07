import math
import unittest
from fractions import Fraction

class NearResonance(unittest.TestCase):
    def test_exact_zero_frequency(self):
        for n in range(1,150):
            x=Fraction(0)
            for k in range(n):
                x=Fraction(k+1,k+2)*x+1
            self.assertEqual(x,Fraction(n*(n+3),2*(n+1)))
    def test_exact_telescope(self):
        for N in range(1,20):
            x=Fraction(3,7)
            s=Fraction(3,7)
            for k in range(N):
                u=Fraction((-1)**k, k+1)
                x=Fraction(k+1,k+2)*x+u
                s+=Fraction(k+2)*u
                self.assertEqual(x,s/Fraction(k+2))
    def test_profile_and_lipschitz(self):
        def h(l,t):
            if l==0: return t/2
            return math.sin(l*t)/l+(math.cos(l*t)-1)/(l*l*t)
        for l in (-3.,-1.,0.,1.,3.):
            for t in (0.1,0.4,1.):
                integral=sum(((i+.5)/10000*t)*math.cos(l*(i+.5)/10000*t) for i in range(10000))*t/10000/t
                self.assertAlmostEqual(h(l,t),integral,delta=1e-7)
                self.assertLessEqual(abs(h(l,t)-h(l+.01,t)),.01*t*t/3+1e-12)
if __name__=='__main__': unittest.main()
