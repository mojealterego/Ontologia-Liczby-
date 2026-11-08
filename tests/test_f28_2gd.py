import math
import unittest
from fractions import Fraction

class MidpointPhaseTests(unittest.TestCase):
    def test_constant_phase_exact_rational(self):
        for n in range(1,101):
            m=sum((Fraction(2*j+1,2*n) for j in range(n)),Fraction(0))/n
            self.assertEqual(m,Fraction(1,2))
    def test_linear_phase_second_order(self):
        for lam in [0.2,1.0,2.0,-3.0]:
            exact=math.sin(lam)/lam+(math.cos(lam)-1)/(lam*lam)
            for n in [5,10,20,50,100]:
                approx=sum((j+.5)/n*math.cos(lam*(j+.5)/n) for j in range(n))/n
                bound=(2*abs(lam)+lam**2)/(24*n*n)
                self.assertLessEqual(abs(exact-approx),bound+1e-12)
    def test_constant_zero_and_pi(self):
        for n in [1,2,3,17,101]:
            self.assertAlmostEqual(sum((j+.5)/n for j in range(n))/n,.5)
            self.assertAlmostEqual(sum(-(j+.5)/n for j in range(n))/n,-.5)
    def test_no_uniform_second_order_lipschitz(self):
        for n in [4,8,16,32]:
            # Integral of t*|t-midpoint| over all cells equals 1/(8*n).
            self.assertEqual(sum((Fraction(j, n)+Fraction(1,2*n))*Fraction(1,4*n*n) for j in range(n)),Fraction(1,8*n))
if __name__=="__main__": unittest.main()
