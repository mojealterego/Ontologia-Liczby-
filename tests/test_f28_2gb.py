import math
import unittest
from fractions import Fraction

class GBTests(unittest.TestCase):
    def test_exact_weights(self):
        for n in range(1, 201):
            q = sum((Fraction(k+2,n*n) for k in range(n)),Fraction(0))
            self.assertEqual(q, Fraction(1,2)+Fraction(3,2*n))
    def test_quadrature_bound(self):
        for n in range(1, 101):
            for a in (0.0,0.3,1.2,math.pi):
                q = sum((k+2)*math.cos(a*k/n) for k in range(n))/n**2
                target = sum((k+.5)/n * math.cos(a*(k+.5)/n) for k in range(n))/n
                self.assertLessEqual(abs(q-target),(abs(a)/2+2.5)/n+1e-12)
    def test_taylor(self):
        for a in (-2.,-1.,0.,1.,2.):
            for h in (-.4,-.1,.1,.4):
                rem = (math.cos(a+h)-math.cos(a)+math.sin(a)*h+math.cos(a)*h*h/2)/2
                self.assertLessEqual(abs(rem),abs(h)**3/12+1e-12)
if __name__ == "__main__":
    unittest.main()
