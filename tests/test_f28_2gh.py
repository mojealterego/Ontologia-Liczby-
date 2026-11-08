import math
import unittest
from fractions import Fraction

class TestF28GH(unittest.TestCase):
    def test_affine_exact(self):
        for n in range(1, 31):
            h = Fraction(1, n)
            for a in (-7, 0, 5):
                for b in (-3, 2):
                    for k in range(1, 10):
                        u = h * Fraction(k, 20)
                        q = sum(h * (a*(j*h+u)+b + a*((j+1)*h-u)+b)/2 for j in range(n))
                        self.assertEqual(q, Fraction(a, 2)+b)
    def test_quadratic_one_cell(self):
        u = Fraction(1, 4)
        self.assertEqual((u*u+(1-u)**2)/2, Fraction(5,16))
        self.assertEqual(Fraction(7,60)-Fraction(1,9), Fraction(1,180))
    def test_curvature_bound_quadratic(self):
        for n in range(1, 51):
            h = Fraction(1,n)
            for k in range(11):
                u = h * Fraction(k,20)
                q = sum(h*((j*h+u)**2+((j+1)*h-u)**2)/2 for j in range(n))
                self.assertLessEqual(abs(q-Fraction(1,3)), Fraction(2,6*n*n))
    def test_phase_curvature(self):
        for lam in (0, 0.2, 1, 3):
            m=2*abs(lam)+lam*lam
            for j in range(101):
                t=j/100
                second=-2*lam*math.sin(lam*t)-t*lam*lam*math.cos(lam*t)
                self.assertLessEqual(abs(second),m+1e-12)

if __name__ == "__main__":
    unittest.main()
