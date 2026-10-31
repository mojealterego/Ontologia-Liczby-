"""Dokładne testy skończonych przypadków dla F18.2; nie zastępują dowodów."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import unittest


def hull_product(a, b, c, d):
    corners = [a*c, a*d, b*c, b*d]
    return min(corners), max(corners)


def clamp(x, a, b):
    return min(b, max(a, x))


class F182ExactTests(unittest.TestCase):
    def setUp(self):
        self.vals = [F(i, j) for i in range(-5, 6) for j in range(1, 5)]

    def test_reverse_triangle(self):
        for x, y in product(self.vals, repeat=2):
            self.assertLessEqual(abs(abs(x)-abs(y)), abs(x-y))

    def test_triangle_equality_sign(self):
        for x, y in product(self.vals, repeat=2):
            self.assertEqual(abs(x+y)==abs(x)+abs(y), x*y>=0)

    def test_clamp_is_nonexpansive(self):
        for x, y in product(self.vals, repeat=2):
            self.assertLessEqual(abs(clamp(x,F(-1,2),F(3,4))-clamp(y,F(-1,2),F(3,4))),abs(x-y))

    def test_interval_distance(self):
        a,b=F(-2,3),F(5,6)
        for x in self.vals:
            self.assertEqual(abs(x-clamp(x,a,b)),max(a-x,F(0),x-b))

    def test_interval_midpoint(self):
        a,b=F(-2,3),F(5,6)
        for k in range(101):
            x=a+(b-a)*F(k,100)
            self.assertLessEqual(abs(x-(a+b)/2),(b-a)/2)

    def test_interval_product(self):
        for a,b,c,d in [(F(-2),F(3),F(-4),F(5)),(F(-4),F(-2),F(-3),F(2)),(F(0),F(1),F(2),F(5))]:
            lo,hi=hull_product(a,b,c,d)
            for i,j in product(range(11),repeat=2):
                x=a+(b-a)*F(i,10);y=c+(d-c)*F(j,10)
                self.assertLessEqual(lo,x*y);self.assertLessEqual(x*y,hi)
            self.assertIn(lo,[a*c,a*d,b*c,b*d]);self.assertIn(hi,[a*c,a*d,b*c,b*d])

    def test_interval_reciprocal_negative(self):
        c,d=F(-4),F(-2)
        for i in range(101):
            y=c+(d-c)*F(i,100)
            self.assertLessEqual(F(1,d),F(1,y));self.assertLessEqual(F(1,y),F(1,c))

    def test_inverse_stability(self):
        for x in self.vals:
            if abs(x)<F(1,2):continue
            for h in [F(-1,4),F(-1,8),F(0),F(1,8),F(1,4)]:
                y=x+h
                self.assertNotEqual(y,0)
                self.assertLessEqual(abs(1/x-1/y),2*abs(h)/F(1,2)**2)

    def test_interval_separation(self):
        cases=[(F(-3),F(-1),F(2),F(5),F(3)),(F(0),F(2),F(1),F(3),F(0)),(F(4),F(5),F(-1),F(2),F(2))]
        for a,b,c,d,expected in cases:
            self.assertEqual(max(F(0),c-b,a-d),expected)

    def test_sqrt2_cauchy_certificate(self):
        qs=[F(isqrt(2*10**(2*n)),10**n) for n in range(1,8)]
        for n,q in enumerate(qs,1):
            self.assertLessEqual(q*q,2)
            self.assertGreater((q+F(1,10**n))**2,2)
        for i in range(len(qs)):
            for j in range(i,len(qs)):
                self.assertLess(abs(qs[i]-qs[j]),F(2,10**(i+1)))

    def test_linear_error_bound(self):
        for dx,dy in product([F(-1,10),F(0),F(1,10)],repeat=2):
            self.assertLessEqual(abs(2*dx-3*dy),2*abs(dx)+3*abs(dy))

    def test_quotient_certificate(self):
        x,xx,y,yy=F(5),F(51,10),F(2),F(21,10)
        bound=F(1,10)/2+2*abs(xx)*F(1,10)/4
        self.assertEqual(bound,F(61,200))
        self.assertEqual(abs(x/y-xx/yy),F(1,14))
        self.assertLessEqual(abs(x/y-xx/yy),bound)

    def test_manuscript_examples(self):
        self.assertEqual(abs(abs(F(-7,3))-abs(F(5,6))),F(3,2))
        self.assertEqual(hull_product(F(-2),F(3),F(-4),F(5)),(F(-12),F(15)))
        self.assertEqual(F(2,10)+F(3,5),F(4,5))


if __name__=='__main__':
    unittest.main()
