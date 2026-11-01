"""Exact finite-field, modular-lifting and rational-interval checks for F23.2.
No floating point; tests verify instances, not general mathematical proofs.
"""
import unittest
from fractions import Fraction
from itertools import product


def gf4_add(a, b):
    return a ^ b


def gf4_mul(a, b):
    p = 0
    for i in range(2):
        for j in range(2):
            if ((a >> i) & 1) and ((b >> j) & 1):
                p ^= 1 << (i + j)
    if p & 8:
        p ^= 0b1100  # x^3 = x^2+x, modulo x^2+x+1
    if p & 4:
        p ^= 0b111
    return p


def gf4_sq(x):
    return gf4_mul(x, x)


def gf4_trace(x):
    return gf4_add(x, gf4_sq(x))


def quadratic_mod(a, b, c, p):
    return [x for x in range(p) if (a*x*x+b*x+c) % p == 0]


def lift_quadratic(a, b, c, p, k, r):
    pk = p**k
    f = a*r*r+b*r+c
    if f % pk:
        raise ValueError('not a root modulo p^k')
    deriv = (2*a*r+b) % p
    if deriv == 0:
        raise ValueError('singular root')
    t = (-(f//pk)*pow(deriv, -1, p)) % p
    rr = r + t*pk
    assert (a*rr*rr+b*rr+c) % (pk*p) == 0
    return rr % (pk*p)


def isolate_quadratic(a, b, c, u, v):
    u, v = Fraction(u), Fraction(v)
    if u >= v:
        return False
    f = lambda x: a*x*x+b*x+c
    du, dv = 2*a*u+b, 2*a*v+b
    return f(u)*f(v) < 0 and ((du > 0 and dv > 0) or (du < 0 and dv < 0))


class F232Certificates(unittest.TestCase):
    def test_gf4_field_table(self):
        for x in range(1, 4):
            self.assertEqual({gf4_mul(x, y) for y in range(4)}, set(range(4)))

    def test_gf4_frobenius(self):
        for x in range(4):
            self.assertEqual(gf4_sq(gf4_sq(x)), x)

    def test_gf4_trace_values(self):
        self.assertEqual([gf4_trace(x) for x in range(4)], [0, 0, 1, 1])

    def test_trace_linearity(self):
        for x, y in product(range(4), repeat=2):
            self.assertEqual(gf4_trace(gf4_add(x,y)), gf4_add(gf4_trace(x), gf4_trace(y)))

    def test_artin_schreier_image(self):
        self.assertEqual({gf4_add(gf4_sq(x),x) for x in range(4)}, {0,1})

    def test_artin_schreier_trace_classification(self):
        for d in range(4):
            roots = [x for x in range(4) if gf4_add(gf4_sq(x),x)==d]
            self.assertEqual(len(roots), 2 if gf4_trace(d)==0 else 0)

    def test_gf4_alpha_roots(self):
        self.assertEqual({x for x in range(4) if gf4_add(gf4_sq(x),x)==1}, {2,3})

    def test_gf4_double_root(self):
        self.assertEqual([x for x in range(4) if gf4_add(gf4_sq(x),1)==0], [1])

    def test_gf4_general_b_nonzero(self):
        for a,b,c in product(range(4),repeat=3):
            if not a or not b:
                continue
            roots = [x for x in range(4) if gf4_add(gf4_add(gf4_mul(a,gf4_sq(x)),gf4_mul(b,x)),c)==0]
            d=gf4_mul(gf4_mul(a,c), next(z for z in range(1,4) if gf4_mul(z,gf4_sq(b))==1))
            self.assertEqual(len(roots), 2 if gf4_trace(d)==0 else 0)

    def test_gf4_general_b_zero(self):
        for a,c in product(range(4),repeat=2):
            if not a:
                continue
            roots=[x for x in range(4) if gf4_add(gf4_mul(a,gf4_sq(x)),c)==0]
            self.assertEqual(len(roots),1)

    def test_odd_discriminant_classification(self):
        for p in (3,5,7,11,13):
            squares={y*y%p for y in range(p)}
            for a,b,c in product(range(p),repeat=3):
                if not a:
                    continue
                delta=(b*b-4*a*c)%p
                expected=1 if delta==0 else 2 if delta in squares else 0
                self.assertEqual(len(quadratic_mod(a,b,c,p)),expected)

    def test_odd_discriminant_example(self):
        self.assertEqual(quadratic_mod(2,3,1,5),[2,4])

    def test_no_integer_root_mod_five(self):
        self.assertEqual(quadratic_mod(1,0,-2,5),[])

    def test_lift_first_root(self):
        self.assertEqual(lift_quadratic(1,0,-2,7,1,3),10)

    def test_lift_second_root(self):
        self.assertEqual(lift_quadratic(1,0,-2,7,1,4),39)

    def test_lift_second_level(self):
        self.assertEqual(lift_quadratic(1,0,-2,7,2,10),108)

    def test_lift_all_simple_quadratics(self):
        for p in (3,5,7):
            for a,b,c in product(range(p),repeat=3):
                if a==0:
                    continue
                roots=quadratic_mod(a,b,c,p)
                if any((2*a*r+b)%p==0 for r in roots):
                    continue
                lifted=[lift_quadratic(a,b,c,p,1,r) for r in roots]
                brute=[r for r in range(p*p) if (a*r*r+b*r+c)%(p*p)==0]
                self.assertEqual(sorted(lifted),brute)

    def test_singular_multiple_lifts(self):
        self.assertEqual([x for x in range(25) if x*x%25==0],[0,5,10,15,20])

    def test_lift_rejects_singular(self):
        with self.assertRaises(ValueError):
            lift_quadratic(1,0,0,5,1,0)

    def test_lift_rejects_nonroot(self):
        with self.assertRaises(ValueError):
            lift_quadratic(1,0,-2,7,1,2)

    def test_interval_isolation(self):
        self.assertTrue(isolate_quadratic(1,0,-2,Fraction(7,5),Fraction(3,2)))

    def test_interval_nonisolation(self):
        self.assertFalse(isolate_quadratic(1,-2,1,0,2))

    def test_exact_residual_bound(self):
        x=Fraction(3,2)
        m=Fraction(14,5)
        self.assertEqual(abs(x*x-2)/m,Fraction(5,56))

    def test_interval_exhaustive_small_roots(self):
        for a,b,c in product(range(-2,3),repeat=3):
            if a==0:
                continue
            for u,v in [(-2,-1),(-1,0),(0,1),(1,2)]:
                if isolate_quadratic(a,b,c,u,v):
                    self.assertNotEqual(a*u*u+b*u+c,0)
                    self.assertNotEqual(a*v*v+b*v+c,0)
                    self.assertNotEqual((2*a*u+b)*(2*a*v+b),0)


if __name__ == '__main__':
    unittest.main()
