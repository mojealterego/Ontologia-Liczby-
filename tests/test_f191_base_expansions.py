"""Dokładne testy F19.1 na Fraction; skończone przypadki, nie mechanizacja dowodów."""
from fractions import Fraction as F
from math import gcd
import unittest


def digits(a, q, b, k):
    assert 0 <= a < q and q > 0 and b >= 2 and k >= 0
    out = []
    r = a
    for _ in range(k):
        r *= b
        d, r = divmod(r, q)
        out.append(d)
    return out, r


def prefix(a, q, b, k):
    return (b**k*a)//q


def finite_length(q, b):
    n = 0
    t = q
    while True:
        g = gcd(t, b)
        if g == 1:
            break
        t //= g
        n += 1
    return n if t == 1 else None


def preperiod_period(q, b):
    n = finite_length(q, b)
    if n is not None:
        return n, 0
    t = q
    N = 0
    while (g := gcd(t, b)) > 1:
        t //= g
        N += 1
    v = b % t
    P = 1
    while v != 1:
        v = (v*b) % t
        P += 1
    return N, P


class F191Tests(unittest.TestCase):
    def test_invariant(self):
        for b in range(2, 13):
            for q in range(2, 34):
                for a in range(q):
                    ds, r = digits(a, q, b, 7)
                    A = sum(d*b**(6-i) for i, d in enumerate(ds))
                    self.assertEqual(F(a,q), F(A,b**7)+F(r,q*b**7))

    def test_digits_bounds(self):
        for b in range(2, 13):
            for q in range(2, 30):
                for a in range(q):
                    ds, r = digits(a,q,b,15)
                    self.assertTrue(all(0 <= d < b for d in ds))
                    self.assertTrue(0 <= r < q)

    def test_prefix_integer_certificate(self):
        for b in range(2, 13):
            for q in range(2, 40):
                for a in range(q):
                    for k in range(5):
                        A=prefix(a,q,b,k)
                        self.assertLessEqual(q*A,b**k*a)
                        self.assertLess(b**k*a,q*(A+1))

    def test_minimal_terminating_length(self):
        for b in range(2, 14):
            for q in range(2, 100):
                if gcd(1,q) != 1: continue
                n=finite_length(q,b)
                if n is not None:
                    self.assertEqual((b**n)%q,0)
                    if n: self.assertNotEqual((b**(n-1))%q,0)
                else:
                    self.assertTrue(all((b**k)%q for k in range(15)))

    def test_exact_preperiod_period(self):
        for b in range(2, 14):
            for q in range(2, 80):
                N,P=preperiod_period(q,b)
                if P:
                    ds,r=digits(1,q,b,N)
                    _,r2=digits(r,q,b,P)
                    self.assertEqual(r,r2)
                    self.assertTrue(all(digits(1,q,b,n)[1] != digits(1,q,b,n+p)[1]
                                        for n in range(N) for p in range(1,P+1)))
                else:
                    self.assertEqual(digits(1,q,b,N)[1],0)

    def test_period_formula(self):
        cases=[(10,1,6,1,6),(10,1,12,2,3),(10,1,28,2,571428)]
        for b,a,q,N,B in cases:
            P=len(str(B))
            # Leading zeros in periodic blocks are supplied by the declared length.
            if q==28: P=6
            if q==12: P=1
            A=prefix(a,q,b,N)
            self.assertEqual(F(a,q),F(A,b**N)+F(B,b**N*(b**P-1)))

    def test_repeating_examples(self):
        self.assertEqual(F(27,99),F(3,11))
        self.assertEqual(F(9,9900),F(1,1100))
        self.assertEqual(F(142857,999999),F(1,7))
        self.assertEqual(F(3,15),F(1,5))

    def test_examples_decimal(self):
        self.assertEqual(prefix(29,125,10,3),232)
        self.assertEqual(prefix(7,40,10,3),175)
        self.assertEqual(preperiod_period(6,10),(1,1))
        self.assertEqual(preperiod_period(28,10),(2,6))
        self.assertEqual(preperiod_period(12,10),(2,1))

    def test_binary_one_fifth(self):
        self.assertEqual(digits(1,5,2,8)[0],[0,0,1,1,0,0,1,1])
        self.assertEqual(F(3,2**4-1),F(1,5))

    def test_two_expansions(self):
        self.assertEqual(F(5,10),F(4,10)+sum((F(9,10**k) for k in range(2,100)),F(0)) + F(1,10**99))
        # Geometric identity is exact without a floating-point limit.
        self.assertEqual(F(4,10)+F(9,90),F(1,2))

    def test_close_numbers_different_cylinders(self):
        x,y=F(4999,10000),F(5001,10000)
        self.assertLess(y-x,F(1,10))
        self.assertNotEqual(prefix(x.numerator,x.denominator,10,1),prefix(y.numerator,y.denominator,10,1))

    def test_cylinder_diameter(self):
        for b in range(2,9):
            for k in range(1,5):
                for A in range(min(b**k,20)):
                    lo,hi=F(A,b**k),F(A+1,b**k)
                    self.assertEqual(hi-lo,F(1,b**k))
                    self.assertLess(lo+(hi-lo)*F(999,1000),hi)


if __name__ == '__main__':
    unittest.main()
