import math
import unittest
from fractions import Fraction

class TestF28GF(unittest.TestCase):
    def test_linear_variance_exact(self):
        for n in range(1,101):
            exact = Fraction(1,12*n**3)
            by_strata = sum((Fraction(1,12*n*n) for _ in range(n)),Fraction(0))/n**2
            self.assertEqual(exact,by_strata)

    def test_shared_shift_variance(self):
        for n in range(1,101):
            independent = Fraction(1,12*n**3)
            shared = Fraction(1,12*n*n)
            self.assertEqual(shared, n*independent)

    def test_phase_lipschitz(self):
        for l in (0.0,0.1,1.0,5.0):
            for a in range(101):
                s=a/100
                for b in range(0,101,5):
                    t=b/100
                    fs=s*math.cos(l*s)
                    ft=t*math.cos(l*t)
                    self.assertLessEqual(abs(fs-ft),(1+l)*abs(s-t)+1e-12)

    def test_certificates(self):
        for n in (1,2,10,100):
            for delta in (0.01,0.05,0.5):
                k=2.5
                radius=k*math.sqrt(math.log(2/delta)/(2*n**3))
                self.assertAlmostEqual(2*math.exp(-2*n**3*radius**2/k**2),delta,places=12)

    def test_budget_phase(self):
        for a in range(-10,11):
            for b in range(-10,11):
                self.assertLessEqual(abs(math.cos(a/10)-math.cos(b/10)),abs(a-b)/10+1e-12)

if __name__=="__main__":
    unittest.main()
