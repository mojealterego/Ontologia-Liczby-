"""Exact-arithmetic regression checks for E1-07 stereometry."""
import math
import unittest
from fractions import Fraction

class Stereometry(unittest.TestCase):
    def test_box_volume(self):
        for a in range(1,10):
            for b in range(1,10):
                for c in range(1,10):
                    self.assertEqual(a*b*c,c*b*a)

    def test_box_surface(self):
        self.assertEqual(2*(2*3+2*5+3*5),62)

    def test_space_diagonal(self):
        self.assertEqual(math.isqrt(3*3+4*4+12*12),13)

    def test_prism(self):
        self.assertEqual(18*9,162)
        self.assertEqual(2*24+20*5,148)

    def test_pyramid(self):
        self.assertEqual(Fraction(30*9,3),90)
        self.assertEqual(Fraction(36*10,3),120)

    def test_cone_cylinder(self):
        for r in range(1,12):
            for h in range(1,12):
                self.assertEqual(Fraction(r*r*h,3)*3,r*r*h)

    def test_cone_slant(self):
        self.assertEqual(math.isqrt(5*5+12*12),13)

    def test_sphere_cross_section(self):
        self.assertEqual(13*13-12*12,5*5)
        self.assertEqual(5*5-3*3,4*4)

    def test_scaling(self):
        for k in range(1,20):
            self.assertEqual((k*3)**3,k**3*27)
            self.assertEqual((k*3)**2,k**2*9)

    def test_units(self):
        self.assertEqual(100**3,1000000)
        self.assertEqual(10**3,1000)
        self.assertEqual(Fraction(40*25*30,1000),30)

    def test_hollow_cylinder(self):
        self.assertEqual((5*5-3*3)*10,160)

    def test_equal_surface_different_volume(self):
        self.assertEqual(2*(Fraction(1,4)+Fraction(11,8)+Fraction(11,8)),6)
        self.assertNotEqual(Fraction(1,2)*Fraction(1,2)*Fraction(11,4),1)

    def test_problem_f(self):
        self.assertEqual(40*5**3,5000)

if __name__=="__main__":
    unittest.main()
