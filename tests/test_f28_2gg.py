import math
import unittest
from fractions import Fraction

class TestF282GG(unittest.TestCase):
    def test_exact_variance_linear(self):
        for n in range(1, 101):
            h=Fraction(1,n)
            var=sum((h*h/Fraction(12))*Fraction(1,n*n) for _ in range(n))
            self.assertEqual(var,Fraction(1,12*n**3))
    def test_concentration_radii(self):
        for n in (1,10,100,1000):
            for m in (1,10,100):
                delta=.05
                r=math.sqrt(math.log(2*m/delta)/(2*n**3))
                self.assertLessEqual(2*m*math.exp(-2*n**3*r*r),delta*(1+1e-12))
    def test_deterministic_bound(self):
        for n in range(1,101):
            for a in (Fraction(0),Fraction(1,2),Fraction(1)):
                h=Fraction(1,n)
                integral=(a*a+(1-a)*(1-a))*h*h/2
                self.assertLessEqual(integral,h*h/2)
    def test_dependent_counterexample(self):
        for n in range(1,100):
            self.assertEqual(Fraction(1,12*n*n),n*Fraction(1,12*n**3))

if __name__=="__main__":
    unittest.main()
