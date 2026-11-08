import unittest
from fractions import Fraction

class AntitheticSharpVariance(unittest.TestCase):
    def test_uniform_moments(self):
        for n in range(1,101):
            h=Fraction(1,n)
            eu2=h*h/12
            eu4=h**4/80
            self.assertEqual(eu4-eu2**2,h**4/180)
    def test_quadratic_exact_variance(self):
        for n in range(1,101):
            h=Fraction(1,n)
            var_one=h**6/180
            self.assertEqual(n*var_one,Fraction(1,180*n**5))
    def test_constants_improve_prior(self):
        self.assertLess(Fraction(1,720),Fraction(1,64))
        self.assertGreater(128,32)
    def test_chebyshev_radius(self):
        self.assertEqual(Fraction(3,1)**2/(720*Fraction(1,20)*10**5),Fraction(1,400000))

if __name__=="__main__":
    unittest.main()
