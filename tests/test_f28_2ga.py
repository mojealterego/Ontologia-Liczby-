import math
import unittest
from fractions import Fraction

class PhaseSensitivity(unittest.TestCase):
    def test_telescope_exact(self):
        for n in range(1, 70):
            b = Fraction(7, 3)
            x = b
            for k in range(n):
                x = Fraction(k+1,k+2)*x + 1
            expected = (b + Fraction(n*(n+3),2))/Fraction(n+1)
            self.assertEqual(x,expected)

    def test_quadratic_remainder(self):
        for n in (1,2,7,32,128):
            weight = (n+3)/(2*(n+1))
            for eps in (-0.7,-0.1,0.0,0.2,0.9):
                self.assertLessEqual(abs(weight*(math.cos(eps)-1)),weight*eps**2/2+1e-14)

    def test_second_order_integral(self):
        for h in (-0.8,-0.3,0.0,0.1,0.6):
            actual = math.cos(h)/2
            approx = 0.5-h*h/4
            self.assertLessEqual(abs(actual-approx),abs(h)**3/12+1e-14)

if __name__=="__main__":
    unittest.main()
