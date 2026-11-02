"""Exact-arithmetic regression checks for E1-06 planimetry."""
import math
import unittest
from fractions import Fraction

class Planimetry(unittest.TestCase):
    def test_triangle_existence(self):
        for a in range(1, 12):
            for b in range(1, 12):
                for c in range(1, 12):
                    geometric = abs(a-b) < c < a+b
                    inequalities = a+b>c and a+c>b and b+c>a
                    self.assertEqual(geometric, inequalities)

    def test_polygon_angle_sum(self):
        for n in range(3, 40):
            self.assertEqual((n-2)*180, n*Fraction((n-2)*180,n))

    def test_diagonal_count(self):
        for n in range(3, 25):
            pairs = sum(1 for i in range(n) for j in range(i+1,n)
                        if j-i not in (1,n-1))
            self.assertEqual(pairs, n*(n-3)//2)

    def test_area_rectangle_optimal(self):
        for p in range(4, 80, 2):
            for a in range(1,p//2):
                b=p//2-a
                if b>0:
                    self.assertLessEqual(Fraction(a*b), Fraction(p*p,16))

    def test_pythagorean_triples(self):
        for a,b,c in ((3,4,5),(5,12,13),(7,24,25),(8,15,17)):
            self.assertEqual(a*a+b*b,c*c)

    def test_trapezoid_area(self):
        self.assertEqual(Fraction(6+10,2)*4,32)

    def test_circle_scaling(self):
        for r in range(1,20):
            for k in range(1,8):
                self.assertEqual((k*r)**2,k*k*r*r)

    def test_triangle_scale_area(self):
        for a in range(1,20):
            for h in range(1,20):
                self.assertEqual(Fraction(3*a*3*h,2),9*Fraction(a*h,2))

    def test_sector_additivity(self):
        for a in range(0,361,10):
            self.assertEqual(Fraction(a,360)+Fraction(360-a,360),1)

    def test_rectangle_diagonal(self):
        self.assertEqual(math.isqrt(6*6+8*8),10)

    def test_counterexamples(self):
        self.assertNotEqual(1*9,5*5)
        self.assertNotEqual(2*2+3*3,4*4)

    def test_worked_problem_f(self):
        self.assertEqual(Fraction(8*5,2),20)
        self.assertEqual(Fraction(8*5,2),Fraction(20*2,2))

if __name__=="__main__":
    unittest.main()
