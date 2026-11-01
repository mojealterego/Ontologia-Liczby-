"""Exact arithmetic regression checks for F24.1; no floating point predicates."""
import unittest
from fractions import Fraction as F
from itertools import product


def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def mul(t, a):
    return (t*a[0], t*a[1])


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def q(a):
    return dot(a, a)


def orient(a, b, c):
    return cross(sub(b, a), sub(c, a))


def projection_t(p, a, b):
    d = sub(b, a)
    if q(d) == 0:
        raise ValueError('degenerate line')
    return F(dot(sub(p, a), d), q(d))


def point_line_d2(p, a, b):
    d = sub(b, a)
    if q(d) == 0:
        raise ValueError('degenerate line')
    return F(cross(d, sub(p, a))**2, q(d))


def point_segment_d2(p, a, b):
    d = sub(b, a)
    if q(d) == 0:
        return q(sub(p, a))
    t = min(F(1), max(F(0), projection_t(p, a, b)))
    return q(sub(p, add(a, mul(t, d))))


def proper_intersection(a, b, c, d):
    return orient(a,b,c)*orient(a,b,d)<0 and orient(c,d,a)*orient(c,d,b)<0


def collinear_interval(a,b,c,d):
    if a==b or orient(a,b,c)!=0 or orient(a,b,d)!=0:
        raise ValueError('requires nondegenerate collinear carrier')
    lo, hi = sorted((projection_t(c,a,b),projection_t(d,a,b)))
    lo, hi = max(F(0),lo), min(F(1),hi)
    return None if lo>hi else (lo,hi)


def circumcenter(a,b,c):
    u,v = sub(b,a),sub(c,a)
    det = cross(u,v)
    if det==0:
        raise ValueError('collinear triangle')
    r,s = F(q(b)-q(a),2),F(q(c)-q(a),2)
    return (F(r*v[1]-u[1]*s,det),F(u[0]*s-r*v[0],det))


class GeometryExactTests(unittest.TestCase):
    def test_01_antisymmetry(self):
        for u,v in product(product(range(-2,3),repeat=2),repeat=2):
            self.assertEqual(cross(u,v),-cross(v,u))
    def test_02_alternating(self):
        for u in product(range(-3,4),repeat=2): self.assertEqual(cross(u,u),0)
    def test_03_cyclic(self):
        for a,b,c in product(product(range(-1,2),repeat=2),repeat=3):
            self.assertEqual(orient(a,b,c),orient(b,c,a))
    def test_04_gram(self):
        for u,v in product(product(range(-3,4),repeat=2),repeat=2):
            self.assertEqual(dot(u,v)**2+cross(u,v)**2,q(u)*q(v))
    def test_05_cauchy(self):
        for u,v in product(product(range(-2,3),repeat=2),repeat=2):
            self.assertLessEqual(dot(u,v)**2,q(u)*q(v))
    def test_06_affine_reflection(self):
        a,b,c=(0,0),(3,0),(1,2)
        reflect=lambda p:(p[0],-p[1])
        self.assertEqual(orient(*map(reflect,(a,b,c))),-orient(a,b,c))
    def test_07_affine_scale(self):
        a,b,c=(0,0),(3,0),(1,2)
        f=lambda p:(2*p[0]+1,3*p[1]-2)
        self.assertEqual(orient(*map(f,(a,b,c))),6*orient(a,b,c))
    def test_08_perpendicular(self): self.assertEqual(dot((2,1),(-1,2)),0)
    def test_09_parallel(self): self.assertEqual(cross((2,1),(6,3)),0)
    def test_10_projection(self): self.assertEqual(projection_t((1,3),(0,0),(4,0)),F(1,4))
    def test_11_projection_rational(self): self.assertEqual(projection_t((1,0),(0,0),(2,2)),F(1,4))
    def test_12_line_distance(self): self.assertEqual(point_line_d2((1,3),(0,0),(4,0)),9)
    def test_13_line_distance_oblique(self): self.assertEqual(point_line_d2((1,0),(0,0),(2,2)),F(1,2))
    def test_14_segment_inside(self): self.assertEqual(point_segment_d2((1,3),(0,0),(4,0)),9)
    def test_15_segment_after(self): self.assertEqual(point_segment_d2((6,3),(0,0),(4,0)),13)
    def test_16_segment_before(self): self.assertEqual(point_segment_d2((-2,3),(0,0),(4,0)),13)
    def test_17_segment_degenerate(self): self.assertEqual(point_segment_d2((3,4),(0,0),(0,0)),25)
    def test_18_line_degenerate_rejected(self):
        with self.assertRaises(ValueError): projection_t((1,0),(0,0),(0,0))
    def test_19_proper_crossing(self): self.assertTrue(proper_intersection((0,0),(4,4),(0,4),(4,0)))
    def test_20_endpoint_not_proper(self): self.assertFalse(proper_intersection((0,0),(2,0),(2,0),(3,1)))
    def test_21_disjoint(self): self.assertFalse(proper_intersection((0,0),(1,0),(3,-1),(3,1)))
    def test_22_collinear_overlap(self): self.assertEqual(collinear_interval((0,0),(4,0),(2,0),(6,0)),(F(1,2),F(1)))
    def test_23_collinear_disjoint(self): self.assertIsNone(collinear_interval((0,0),(1,0),(2,0),(3,0)))
    def test_24_collinear_singleton(self): self.assertEqual(collinear_interval((0,0),(2,0),(2,0),(3,0)),(F(1),F(1)))
    def test_25_circumcenter_right(self): self.assertEqual(circumcenter((0,0),(2,0),(0,2)),(F(1),F(1)))
    def test_26_circumcenter_shift(self): self.assertEqual(circumcenter((1,1),(5,1),(1,3)),(F(3),F(2)))
    def test_27_circumcenter_collinear(self):
        with self.assertRaises(ValueError): circumcenter((0,0),(1,1),(2,2))
    def test_28_circumcenter_equidistant_exhaustive(self):
        pts=list(product(range(-1,2),repeat=2))
        for a,b,c in product(pts,repeat=3):
            if orient(a,b,c):
                o=circumcenter(a,b,c)
                self.assertEqual(q(sub(o,a)),q(sub(o,b)))
                self.assertEqual(q(sub(o,a)),q(sub(o,c)))
    def test_29_point_segment_lower_bound(self):
        for p in product(range(-3,4),repeat=2):
            self.assertGreaterEqual(point_segment_d2(p,(0,0),(2,1)),0)
    def test_30_solved_examples(self):
        self.assertEqual(orient((0,0),(3,0),(1,2)),6)
        self.assertEqual(dot((1,1),(-2,1)),-1)
        self.assertEqual(cross((1,1),(-2,1)),3)

if __name__=='__main__': unittest.main()
