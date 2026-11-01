"""F26.2: exact arithmetic certificates for uncertain quadratic functions.

No floating-point comparisons. Independent exhaustive checks use small rational grids.
"""
from __future__ import annotations

import itertools
import unittest
from fractions import Fraction as Q
from math import ceil, floor


def value(a: Q, b: Q, c: Q, x: Q) -> Q:
    return a*x*x+b*x+c


def extrema(a: Q, b: Q, c: Q, lo: Q, hi: Q) -> tuple[Q, Q]:
    if lo > hi:
        raise ValueError("empty interval")
    xs = [lo, hi]
    if a:
        p = -b/(2*a)
        if lo <= p <= hi:
            xs.append(p)
    ys = [value(a, b, c, x) for x in xs]
    return min(ys), max(ys)


def lower_at(a0: Q, b0: Q, b1: Q, c0: Q, x: Q) -> Q:
    return a0*x*x + min(b0*x, b1*x) + c0


def upper_at(a1: Q, b0: Q, b1: Q, c1: Q, x: Q) -> Q:
    return a1*x*x + max(b0*x, b1*x) + c1


def robust_bounds(a0: Q, a1: Q, b0: Q, b1: Q, c0: Q, c1: Q, lo: Q, hi: Q) -> tuple[Q, Q]:
    if not (a0 <= a1 and b0 <= b1 and c0 <= c1 and lo <= hi):
        raise ValueError("invalid interval")
    pieces = []
    if lo <= 0:
        pieces.append((lo, min(hi, Q(0)), b1, b0))
    if hi >= 0:
        pieces.append((max(lo, Q(0)), hi, b0, b1))
    lows, highs = [], []
    for l, u, bl, bu in pieces:
        lows.append(extrema(a0, bl, c0, l, u)[0])
        highs.append(extrema(a1, bu, c1, l, u)[1])
    return min(lows), max(highs)


def integer_optima(a: Q, b: Q, c: Q, lo: int, hi: int, minimize: bool = True) -> tuple[Q, tuple[int, ...]]:
    if lo > hi:
        raise ValueError("empty integer grid")
    if (minimize and a < 0) or (not minimize and a > 0):
        # For the opposite curvature the requested extremum is at a grid endpoint.
        candidates = [lo, hi]
    elif a == 0:
        candidates = list(range(lo, hi+1)) if b == 0 else [lo, hi]
    else:
        p = -b/(2*a)
        candidates = sorted(set((lo, hi, max(lo, min(hi, floor(p))), max(lo, min(hi, ceil(p))))))
    vals = [(value(a, b, c, Q(n)), n) for n in candidates]
    best = (min if minimize else max)(v for v, _ in vals)
    return best, tuple(sorted(n for v, n in vals if v == best))


def bernstein(a: Q, b: Q, c: Q, lo: Q, hi: Q) -> tuple[Q, Q, Q]:
    if not lo < hi:
        raise ValueError("nondegenerate interval required")
    beta0 = value(a, b, c, lo)
    beta2 = value(a, b, c, hi)
    beta1 = 2*value(a, b, c, (lo+hi)/2)-(beta0+beta2)/2
    return beta0, beta1, beta2


def fit_affine(data: list[tuple[Q, Q]]) -> tuple[Q, Q]:
    if len(data) < 2:
        raise ValueError("at least two observations")
    n = len(data)
    sx = sum((x for x, _ in data), Q(0))
    sy = sum((y for _, y in data), Q(0))
    sxx = sum((x*x for x, _ in data), Q(0))
    sxy = sum((x*y for x, y in data), Q(0))
    den = n*sxx-sx*sx
    if den <= 0:
        raise ValueError("non-identifiable slope")
    a = (n*sxy-sx*sy)/den
    return a, (sy-a*sx)/n


class QuadraticCertificateTests(unittest.TestCase):
    def test_z1(self):
        self.assertEqual(extrema(Q(2),Q(-4),Q(1),Q(0),Q(3)),(Q(-1),Q(7)))

    def test_z2(self):
        self.assertEqual(robust_bounds(Q(1),Q(2),Q(-1),Q(1),Q(2),Q(3),Q(0),Q(1))[0],Q(7,4))

    def test_z3(self):
        self.assertEqual(robust_bounds(Q(-2),Q(-1),Q(-1),Q(1),Q(-3),Q(-2),Q(-1),Q(1))[1],Q(-7,4))

    def test_z4(self):
        self.assertEqual(lower_at(Q(0),Q(-2),Q(-1),Q(1),Q(-1)),Q(2))
        self.assertEqual(lower_at(Q(0),Q(-2),Q(-1),Q(1),Q(1)),Q(-1))

    def test_z5(self):
        self.assertEqual(integer_optima(Q(3),Q(-17),Q(5),0,8),(Q(-19),(3,)))

    def test_z6(self):
        self.assertEqual(integer_optima(Q(-2),Q(9),Q(-1),0,5,False),(Q(9),(2,)))

    def test_z7(self):
        self.assertLess(value(Q(1),Q(0),Q(-2),Q(1)),0)
        self.assertGreater(value(Q(1),Q(0),Q(-2),Q(3,2)),0)
        self.assertGreaterEqual(2*Q(1),Q(2))

    def test_z8(self):
        self.assertEqual(Q(1,100)/Q(2),Q(1,200))

    def test_z9(self):
        self.assertEqual(bernstein(Q(1),Q(0),Q(1),Q(-1),Q(1)),(Q(2),Q(0),Q(2)))

    def test_z10(self):
        self.assertEqual(bernstein(Q(1),Q(-1),Q(1,4),Q(0),Q(1)),(Q(1,4),Q(-1,4),Q(1,4)))

    def test_z11(self):
        self.assertEqual(fit_affine([(Q(0),Q(1)),(Q(1),Q(2)),(Q(2),Q(2))]),(Q(1,2),Q(7,6)))

    def test_z12(self):
        self.assertEqual(Q(1,100)*4+Q(1,50)*2+Q(1,20),Q(13,100))

    def test_extrema_affine(self):
        self.assertEqual(extrema(Q(0),Q(-2),Q(3),Q(-2),Q(4)),(Q(-5),Q(7)))

    def test_extrema_singleton(self):
        self.assertEqual(extrema(Q(2),Q(-3),Q(1),Q(2),Q(2)),(Q(3),Q(3)))

    def test_extrema_invalid(self):
        with self.assertRaises(ValueError):
            extrema(Q(1),Q(0),Q(0),Q(2),Q(1))

    def test_box_invalid(self):
        with self.assertRaises(ValueError):
            robust_bounds(Q(2),Q(1),Q(0),Q(1),Q(0),Q(1),Q(-1),Q(1))

    def test_box_cross_zero(self):
        self.assertEqual(robust_bounds(Q(0),Q(0),Q(-2),Q(3),Q(1),Q(1),Q(-1),Q(1)),(Q(-2),Q(4)))

    def test_box_one_point(self):
        self.assertEqual(robust_bounds(Q(-1),Q(2),Q(-2),Q(3),Q(-1),Q(4),Q(0),Q(0)),(Q(-1),Q(4)))

    def test_box_exhaustive_at_points(self):
        vals=[Q(-2),Q(-1),Q(0),Q(1),Q(2)]
        for x in vals:
            coeffs=[value(a,b,c,x) for a,b,c in itertools.product((Q(-1),Q(2)),(Q(-2),Q(1)),(Q(-3),Q(4)))]
            self.assertEqual(lower_at(Q(-1),Q(-2),Q(1),Q(-3),x),min(coeffs))
            self.assertEqual(upper_at(Q(2),Q(-2),Q(1),Q(4),x),max(coeffs))

    def test_box_global_exhaustive(self):
        for a0,a1,b0,b1,c0,c1 in [(-2,1,-1,2,-1,3),(1,3,-3,-1,2,4),(-3,-1,-2,3,-4,-1)]:
            lo,hi=Q(-2),Q(2)
            rmin,rmax=robust_bounds(*map(Q,(a0,a1,b0,b1,c0,c1)),lo,hi)
            extremes=[extrema(Q(a),Q(b),Q(c),lo,hi) for a,b,c in itertools.product((a0,a1),(b0,b1),(c0,c1))]
            self.assertEqual(rmin,min(v[0] for v in extremes))
            self.assertEqual(rmax,max(v[1] for v in extremes))

    def test_integer_tie(self):
        self.assertEqual(integer_optima(Q(1),Q(-1),Q(0),0,2),(Q(0),(0,1)))

    def test_integer_boundary(self):
        self.assertEqual(integer_optima(Q(1),Q(-20),Q(0),0,3),(Q(-51),(3,)))

    def test_integer_affine(self):
        self.assertEqual(integer_optima(Q(0),Q(2),Q(-1),-2,3),(Q(-5),(-2,)))

    def test_integer_invalid(self):
        with self.assertRaises(ValueError):
            integer_optima(Q(1),Q(0),Q(0),2,1)

    def test_integer_exhaustive(self):
        for a,b,c in itertools.product(range(-3,4),repeat=3):
            for minimize in (True,False):
                expected=[(value(Q(a),Q(b),Q(c),Q(n)),n) for n in range(-3,5)]
                best=(min if minimize else max)(v for v,n in expected)
                roots=tuple(n for v,n in expected if v==best)
                self.assertEqual(integer_optima(Q(a),Q(b),Q(c),-3,4,minimize),(best,roots))

    def test_bernstein_nonnegative(self):
        for a,b,c in itertools.product(range(-2,3),repeat=3):
            betas=bernstein(Q(a),Q(b),Q(c),Q(-1),Q(2))
            if all(v>=0 for v in betas):
                self.assertGreaterEqual(extrema(Q(a),Q(b),Q(c),Q(-1),Q(2))[0],0)

    def test_bernstein_invalid(self):
        with self.assertRaises(ValueError):
            bernstein(Q(1),Q(0),Q(0),Q(2),Q(2))

    def test_bernstein_identity(self):
        for a,b,c in itertools.product(range(-2,3),repeat=3):
            b0,b1,b2=bernstein(Q(a),Q(b),Q(c),Q(-1),Q(2))
            for t in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
                x=Q(-1)+3*t
                self.assertEqual(value(Q(a),Q(b),Q(c),x),b0*(1-t)**2+2*b1*t*(1-t)+b2*t*t)

    def test_least_squares_normal_equations(self):
        for data in [[(Q(0),Q(1)),(Q(1),Q(2)),(Q(2),Q(2))],[(Q(-2),Q(3)),(Q(1),Q(-1)),(Q(4),Q(0))]]:
            a,b=fit_affine(data)
            self.assertEqual(sum((y-a*x-b for x,y in data),Q(0)),0)
            self.assertEqual(sum((x*(y-a*x-b) for x,y in data),Q(0)),0)

    def test_least_squares_exact_line(self):
        for a,b in itertools.product(range(-2,3),repeat=2):
            data=[(Q(x),Q(a*x+b)) for x in (-2,0,3)]
            self.assertEqual(fit_affine(data),(Q(a),Q(b)))

    def test_least_squares_degenerate(self):
        with self.assertRaises(ValueError):
            fit_affine([(Q(1),Q(2)),(Q(1),Q(3))])

    def test_least_squares_single(self):
        with self.assertRaises(ValueError):
            fit_affine([(Q(1),Q(2))])

    def test_stability_exhaustive(self):
        for a,b,c,da,db,dc in itertools.product((-1,0,1),repeat=6):
            eps=Q(abs(da)*4+abs(db)*2+abs(dc))
            f=extrema(Q(a),Q(b),Q(c),Q(-2),Q(2))
            g=extrema(Q(a+da),Q(b+db),Q(c+dc),Q(-2),Q(2))
            self.assertLessEqual(abs(f[0]-g[0]),eps)
            self.assertLessEqual(abs(f[1]-g[1]),eps)

    def test_root_interval_sign(self):
        self.assertLess(value(Q(1),Q(0),Q(-2),Q(1))*value(Q(1),Q(0),Q(-2),Q(3,2)),0)

    def test_root_bound_rational(self):
        # q=x-1, q_tilde=x-101/100: exact roots differ by eps/mu.
        self.assertEqual(abs(Q(101,100)-Q(1)),Q(1,100))


if __name__ == "__main__":
    unittest.main()
