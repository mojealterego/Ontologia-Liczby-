import math
import random
import unittest
from fractions import Fraction

class StratifiedQuadrature(unittest.TestCase):
    def test_constant_phase_exact_moments(self):
        for n in range(1,101):
            self.assertEqual(Fraction(1,2), sum((Fraction(2*j+1,2*n) for j in range(n)),Fraction(0))/n)
            self.assertEqual(Fraction(1,12*n**3), Fraction(1,12*n**3))
    def test_common_shift_counterexample(self):
        for n in range(1,101):
            v=Fraction(1,3)
            samples=[Fraction(j, n)+v/n for j in range(n)]
            s=sum(samples,Fraction(0))/n
            self.assertEqual(s,Fraction(n-1,2*n)+v/n)
    def test_lipschitz_certificates(self):
        for n in (1,2,3,5,10,25,100):
            for lam in (-5.,-1.,0.,0.5,3.):
                k=1+abs(lam)
                f=lambda t:t*math.cos(lam*t)
                approx=sum(f((j+0.5)/n) for j in range(n))/n
                integral=0.5 if lam==0 else math.sin(lam)/lam+(math.cos(lam)-1)/lam**2
                self.assertLessEqual(abs(approx-integral),k/(2*n)+1e-12)
    def test_empirical_unbiasedness(self):
        rng=random.Random(20261108)
        n=8
        vals=[]
        for _ in range(20000):
            vals.append(sum((j+rng.random())/n for j in range(n))/n)
        self.assertLess(abs(sum(vals)/len(vals)-0.5),0.005)
if __name__=="__main__":
    unittest.main()
