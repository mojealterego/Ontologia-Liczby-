"""Exact arithmetic regression checks for F24.2 (not a formal proof assistant)."""
from __future__ import annotations

import math
import unittest
from fractions import Fraction as Q
from itertools import product


def shoelace_twice(poly):
    if len(poly) < 3:
        raise ValueError('At least three vertices required')
    return sum((Q(x) * Q(poly[(i + 1) % len(poly)][1]) -
                Q(y) * Q(poly[(i + 1) % len(poly)][0]))
               for i, (x, y) in enumerate(poly))


def area(poly):
    return abs(shoelace_twice(poly)) / 2


def boundary(poly):
    if any(not isinstance(z, int) for p in poly for z in p):
        raise TypeError('Integer vertices required')
    return sum(math.gcd(abs(x - poly[i-1][0]), abs(y - poly[i-1][1]))
               for i, (x, y) in enumerate(poly))


def on_segment(p, a, b):
    (x, y), (ax, ay), (bx, by) = p, a, b
    return ((bx-ax)*(y-ay) == (by-ay)*(x-ax) and
            min(ax, bx) <= x <= max(ax, bx) and
            min(ay, by) <= y <= max(ay, by))


def inside_open(p, poly):
    """Exact odd-even ray test for simple polygons; boundary excluded."""
    if any(on_segment(p, poly[i-1], poly[i]) for i in range(len(poly))):
        return False
    x, y = p
    crossings = 0
    for i, (ax, ay) in enumerate(poly):
        bx, by = poly[(i+1) % len(poly)]
        if (ay > y) != (by > y):
            xcross = Q(ax) + Q(y-ay)*Q(bx-ax, by-ay)
            if xcross > x:
                crossings += 1
    return bool(crossings % 2)


def brute_interior(poly, holes=()):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    result = 0
    for x in range(min(xs)+1, max(xs)):
        for y in range(min(ys)+1, max(ys)):
            p = (x,y)
            if inside_open(p, poly) and not any(
                    inside_open(p,h) or any(on_segment(p,h[i-1],h[i])
                                             for i in range(len(h)))
                    for h in holes):
                result += 1
    return result


def pick(poly):
    return Q(brute_interior(poly)) + Q(boundary(poly), 2) - 1


def pick_holes(outer, holes):
    b = boundary(outer) + sum(boundary(h) for h in holes)
    i = brute_interior(outer, holes)
    return Q(i) + Q(b,2) - 1 + len(holes)


def rect(x0, y0, w, h):
    if w <= 0 or h <= 0:
        raise ValueError('positive dimensions required')
    return [(x0,y0),(x0+w,y0),(x0+w,y0+h),(x0,y0+h)]


class AreaCertificateTests(unittest.TestCase):
    def test_z1_triangle(self):
        p=[(0,0),(5,0),(0,3)]
        self.assertEqual((area(p),boundary(p),brute_interior(p)),(Q(15,2),9,4))

    def test_z2_square(self):
        p=rect(0,0,4,4)
        self.assertEqual((area(p),boundary(p),brute_interior(p)),(16,16,9))

    def test_z3_triangle(self):
        p=[(0,0),(3,0),(0,2)]
        self.assertEqual((area(p),boundary(p),brute_interior(p)),(3,6,1))

    def test_z4_parallelogram(self):
        p=[(0,0),(3,1),(5,4),(2,3)]
        self.assertEqual((area(p),boundary(p),brute_interior(p)),(7,4,6))

    def test_z5_concave(self):
        p=[(0,0),(3,0),(3,1),(1,1),(1,3),(0,3)]
        self.assertEqual((area(p),boundary(p),brute_interior(p)),(5,12,0))

    def test_z6_hole(self):
        outer=rect(0,0,4,4); hole=rect(1,1,2,2)
        self.assertEqual((area(outer)-area(hole),pick_holes(outer,[hole])),(12,12))
        self.assertEqual(brute_interior(outer,[hole]),0)

    def test_z7_rational(self):
        p=[(Q(0),Q(0)),(Q(1,2),Q(0)),(Q(0),Q(1,2))]
        self.assertEqual(area(p),Q(1,8))
        q=[(2*x,2*y) for x,y in p]
        self.assertEqual(area(q)/4,Q(1,8))

    def test_z8_orientation(self):
        p=[(0,0),(5,0),(0,3)]
        self.assertEqual(shoelace_twice(p),-shoelace_twice(p[::-1]))

    def test_z9_shear(self):
        p=[(0,0),(5,0),(0,3)]
        q=[(x+2*y,y) for x,y in p]
        self.assertEqual((area(q),boundary(q),brute_interior(q)),(Q(15,2),9,4))

    def test_z10_bound(self):
        n,M,eps=3,10,Q(1,100)
        self.assertEqual(n*(2*M*eps+eps**2),Q(6003,10000))

    def test_z11_empty_interior(self):
        p=[(0,0),(2,0),(1,1)]
        self.assertEqual((area(p),boundary(p),brute_interior(p)),(1,4,0))

    def test_z12_second_hole(self):
        outer=rect(0,0,5,5); hole=rect(2,2,1,1)
        self.assertEqual((brute_interior(outer,[hole]),pick_holes(outer,[hole])),(12,24))

    def test_k1_bowtie_signed_zero(self):
        p=[(0,0),(2,2),(0,2),(2,0)]
        self.assertEqual(shoelace_twice(p),0)

    def test_k2_boundary_not_vertices(self):
        self.assertEqual(boundary(rect(0,0,2,2)),8)

    def test_k3_missing_hole_correction(self):
        o=rect(0,0,4,4); h=rect(1,1,2,2)
        self.assertEqual(pick_holes(o,[h])-1,11)

    def test_k4_nonlattice(self):
        p=[(0,0),(Q(1,2),0),(0,Q(1,2))]
        with self.assertRaises(TypeError): boundary(p)

    def test_k5_singular_affine(self):
        p=rect(0,0,2,2)
        q=[(x,0) for x,y in p]
        self.assertEqual((area(p),area(q)),(4,0))

    def test_k6_float_cancellation(self):
        n=10**16
        p=[(n,n),(n+1,n),(n,n+1)]
        self.assertEqual(area(p),Q(1,2))
        self.assertEqual(area([(float(x),float(y)) for x,y in p]),0)

    def test_primitive_triangles(self):
        for p in ([ (0,0),(1,0),(0,1)],[(1,2),(2,2),(1,3)],[(0,0),(2,1),(1,1)]):
            self.assertEqual(area(p),Q(1,2))
            self.assertEqual(brute_interior(p),0)
            self.assertEqual(boundary(p),3)

    def test_pick_exhaustive_rectangles(self):
        for x,y,w,h in product(range(-2,3),range(-2,3),range(1,5),range(1,5)):
            p=rect(x,y,w,h)
            self.assertEqual(area(p),pick(p))

    def test_pick_exhaustive_axis_triangles(self):
        for x,y,a,b in product(range(-1,2),range(-1,2),range(1,7),range(1,7)):
            p=[(x,y),(x+a,y),(x,y+b)]
            self.assertEqual(area(p),pick(p))

    def test_pick_reflections(self):
        p=[(0,0),(3,0),(3,1),(1,1),(1,3),(0,3)]
        for a,b in [(1,1),(-1,1),(1,-1),(-1,-1)]:
            q=[(a*x,b*y) for x,y in p]
            self.assertEqual(area(q),pick(q))
            self.assertEqual((boundary(q),brute_interior(q)),(12,0))

    def test_pick_translations(self):
        p=[(0,0),(5,0),(0,3)]
        for dx,dy in product(range(-3,4),repeat=2):
            q=[(x+dx,y+dy) for x,y in p]
            self.assertEqual((area(q),boundary(q),brute_interior(q)),(Q(15,2),9,4))

    def test_holes_exhaustive_nested_rectangles(self):
        for w,h in product(range(3,7),repeat=2):
            outer=rect(0,0,w,h)
            for a,b in product(range(1,w-1),range(1,h-1)):
                hole=rect(a,b,1,1)
                self.assertEqual(area(outer)-area(hole),pick_holes(outer,[hole]))

    def test_two_holes(self):
        outer=rect(0,0,8,5)
        holes=[rect(1,1,1,1),rect(5,2,2,2)]
        self.assertEqual(pick_holes(outer,holes),area(outer)-sum(map(area,holes)))

    def test_reversed_hole_boundary(self):
        o=rect(0,0,4,4); h=rect(1,1,2,2)
        self.assertEqual((shoelace_twice(o)+shoelace_twice(h[::-1]))/2,12)

    def test_rational_denominator_property(self):
        for d in range(1,9):
            p=[(Q(0),Q(0)),(Q(1,d),Q(0)),(Q(0),Q(1,d))]
            self.assertEqual(2*d*d*area(p),1)

    def test_affine_unimodular(self):
        p=[(0,0),(5,0),(0,3)]
        for k in range(-4,5):
            q=[(x+k*y,y) for x,y in p]
            self.assertEqual((area(q),boundary(q),brute_interior(q)),(Q(15,2),9,4))

    def test_perturbation_bound_samples(self):
        p=[(1,2),(3,1),(-2,4),(0,-3)]
        eps=Q(1,10); M=4
        base=shoelace_twice(p)/2
        for dx,dy in product((-eps,0,eps),repeat=2):
            q=[(Q(x)+dx,Q(y)+dy) for x,y in p]
            self.assertLessEqual(abs(shoelace_twice(q)/2-base),len(p)*(2*M*eps+eps*eps))

    def test_collinear_edges(self):
        p=[(0,0),(1,0),(2,0),(2,2),(0,2)]
        self.assertEqual((area(p),boundary(p),brute_interior(p)),(4,8,1))

    def test_shoelace_cyclic_shift(self):
        p=[(0,0),(3,0),(3,1),(1,1),(1,3),(0,3)]
        for i in range(len(p)):
            self.assertEqual(shoelace_twice(p),shoelace_twice(p[i:]+p[:i]))

    def test_shoelace_translation(self):
        p=[(0,0),(5,0),(0,3)]
        q=[(x+100000,y-200000) for x,y in p]
        self.assertEqual(shoelace_twice(p),shoelace_twice(q))

    def test_shoelace_rational_fraction(self):
        p=[(Q(1,3),Q(1,7)),(Q(5,3),Q(1,7)),(Q(1,3),Q(4,7))]
        self.assertEqual(area(p),Q(2,7))

    def test_reject_degenerate_rect(self):
        with self.assertRaises(ValueError): rect(0,0,0,1)

    def test_reject_short_polygon(self):
        with self.assertRaises(ValueError): shoelace_twice([(0,0),(1,1)])


if __name__ == '__main__':
    unittest.main()
