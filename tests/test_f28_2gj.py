"""Exact regression tests for F28.2-GJ; stdlib only."""
import unittest
from fractions import Fraction as F

class NonuniformAntithetic(unittest.TestCase):
    def test_uniform_optimum(self):
        for n in range(1, 101):
            h = [F(1,n)]*n
            self.assertEqual(sum(x**6 for x in h), F(1,n**5))

    def test_quadratic_exact_variance(self):
        # Var(U^2), U~Uniform(0,h/2), computed from exact moments.
        for n in range(1, 31):
            h=F(1,n)
            var_u2=h**4/F(80)-h**4/F(144)
            self.assertEqual(var_u2,h**4/F(180))
            self.assertEqual(n*h*h*var_u2,F(1,180*n**5))

    def test_nonuniform(self):
        h=[F(1,4),F(3,4)]
        energy=sum(x**6 for x in h)
        self.assertEqual(energy,F(365,2048))
        self.assertGreater(energy,F(1,32))
        self.assertEqual(energy/F(180),F(73,73728))

    def test_dependence_counterexample(self):
        for n in range(2, 25):
            h=[F(1,n)]*n
            shared=(sum(x**3 for x in h))**2/F(180)
            independent=sum(x**6 for x in h)/F(180)
            self.assertEqual(shared,F(1,180*n**4))
            self.assertEqual(independent,F(1,180*n**5))
            self.assertEqual(shared/independent,n)

    def test_affine_exactness(self):
        h=[F(1,5),F(1,3),F(7,15)]
        x=F(0)
        total=F(0)
        for width in h:
            mid=x+width/2
            total+=width*(3*mid-7)
            x+=width
        self.assertEqual(x,1)
        self.assertEqual(total,F(3,2)-7)

if __name__=="__main__":
    unittest.main()
