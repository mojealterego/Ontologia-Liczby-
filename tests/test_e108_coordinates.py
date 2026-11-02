"""E1-08: exact coordinate geometry regression/property checks (standard library)."""
from fractions import Fraction as F
from itertools import product
import unittest

def det(u, v):
    return u[0]*v[1] - u[1]*v[0]

def diff(a, b):
    return b[0]-a[0], b[1]-a[1]

def norm2(v):
    return v[0]*v[0] + v[1]*v[1]

def area2(a, b, c):
    return abs(det(diff(a,b), diff(a,c)))

def line_intersection(a,b,c,d,e,f):
    delta = a*e-d*b
    if delta == 0:
        raise ValueError("parallel or coincident")
    return F(c*e-f*b, delta), F(a*f-d*c, delta)

class CoordinateGeometryTests(unittest.TestCase):
    def test_distance_symmetry_and_zero(self):
        pts = list(product(range(-2,3), repeat=2))
        for a in pts:
            self.assertEqual(norm2(diff(a,a)),0)
            for b in pts:
                self.assertEqual(norm2(diff(a,b)),norm2(diff(b,a)))
                self.assertEqual(norm2(diff(a,b))==0,a==b)

    def test_midpoint(self):
        for a in product(range(-3,4),repeat=2):
            for b in [(2,5),(-4,1),(0,0)]:
                m=((F(a[0]+b[0],2)),F(a[1]+b[1],2))
                self.assertEqual(diff(a,m),diff(m,b))

    def test_partition(self):
        a=(F(2),F(2));b=(F(10),F(6));t=F(3,4)
        p=tuple((1-t)*a[i]+t*b[i] for i in range(2))
        self.assertEqual(p,(F(8),F(5)))
        self.assertEqual(norm2(diff(a,p)),t*t*norm2(diff(a,b)))

    def test_collinearity(self):
        self.assertEqual(det((2,2),(5,5)),0)
        self.assertEqual(det((2,2),(5,4)),-2)

    def test_signed_area_translation(self):
        a=(1,1);b=(5,1);c=(1,4)
        for t in product(range(-5,6),repeat=2):
            shifted=[(p[0]+t[0],p[1]+t[1]) for p in (a,b,c)]
            self.assertEqual(area2(*shifted),12)

    def test_dot_product_perpendicular(self):
        self.assertEqual((2*-3)+(3*2),0)
        self.assertNotEqual((2*3)+(3*2),0)

    def test_line_intersections(self):
        self.assertEqual(line_intersection(1,1,5,1,-1,1),(F(3),F(2)))
        self.assertEqual(line_intersection(2,1,7,1,-1,2),(F(3),F(1)))
        with self.assertRaises(ValueError):
            line_intersection(1,1,1,2,2,3)

    def test_point_line_distance_squared(self):
        a,b,c=3,4,-20
        p=(0,0)
        distance_squared=F((a*p[0]+b*p[1]+c)**2,a*a+b*b)
        self.assertEqual(distance_squared,16)

    def test_reflections(self):
        for x,y in product(range(-4,5),repeat=2):
            self.assertEqual(norm2((x,-y)),norm2((x,y)))
            self.assertEqual(norm2((-x,y)),norm2((x,y)))
            self.assertEqual(norm2((-x,-y)),norm2((x,y)))

    def test_shoelace(self):
        poly=[(0,0),(5,0),(5,2),(0,2)]
        s=sum(det(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))
        self.assertEqual(abs(s),20)

    def test_circle(self):
        self.assertEqual(norm2((3,4)),25)
        self.assertNotEqual(norm2((3,3)),25)

    def test_square(self):
        a,b,c,d=(0,0),(2,1),(1,3),(-1,2)
        vectors=[diff(a,b),diff(b,c),diff(c,d),diff(d,a)]
        self.assertEqual(set(map(norm2,vectors)),{5})
        self.assertEqual(sum(vectors[0][i]*vectors[1][i] for i in range(2)),0)

if __name__=="__main__":
    unittest.main()
