"""F23.3: dokładne kontrole nierówności, przedziałów i ciągu Sturma.

Testy skończone nie zastępują dowodów ogólnych.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as F
from itertools import product
from sympy import Poly, QQ, Rational, symbols

X = symbols("x")


def sign(q):
    return 1 if q > 0 else (-1 if q < 0 else 0)


def interval_product(a, b):
    v = [u * w for u, w in product(a, b)]
    return min(v), max(v)


def interval_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def horner_interval(coefficients_high_to_low, a, b):
    out = (F(coefficients_high_to_low[0]),) * 2
    for c in coefficients_high_to_low[1:]:
        out = interval_add(interval_product((a, b), out), (F(c), F(c)))
    return out


def sturm_variations(poly, at):
    p = Poly(poly, X, domain=QQ)
    seq = [p, p.diff()]
    if p.degree() < 1 or p.gcd(seq[1]).degree() > 0:
        raise ValueError("Wymagany wielomian bezkwadratowy stopnia dodatniego")
    while seq[-1].degree() > 0:
        r = -seq[-2].rem(seq[-1])
        seq.append(r)
    signs = [sign(s.eval(Rational(at.numerator, at.denominator))) for s in seq]
    if 0 in signs:
        raise ValueError("Punkt końcowy zeruje element ciągu Sturma")
    return sum(a != b for a, b in zip(signs, signs[1:]))


def ratio_condition(p, q, x, op):
    num, den = p(x), q(x)
    if den == 0:
        return False
    v = num / den
    return {"ge": v >= 0, "gt": v > 0, "le": v <= 0}[op]


class InequalityCertificates(unittest.TestCase):
    def test_t1_sign_equivalence(self):
        for a, b, x in product(range(-4, 5), repeat=3):
            p, q = a*x+b, x*x-2
            if q:
                self.assertEqual(sign(F(p, q)), sign(p*q))

    def test_t2_cell_sign(self):
        for x in [F(-7), F(-3), F(-2), F(0), F(1), F(4)]:
            p, q = x-2, x+1
            if q:
                self.assertEqual(sign(F(p, q)), sign(p*q))

    def test_t3_strict_monotonicity(self):
        xs = [F(i, 10) for i in range(13, 22)]
        self.assertTrue(all(a**3-2 < b**3-2 for a, b in zip(xs, xs[1:])))

    def test_t4_horner_soundness(self):
        for a, b in [(F(-2), F(3)), (F(0), F(1)), (F(3, 2), F(2))]:
            lo, hi = horner_interval([2, -3, 1], a, b)
            for j in range(51):
                x = a+(b-a)*F(j, 50)
                self.assertLessEqual(lo, 2*x*x-3*x+1)
                self.assertLessEqual(2*x*x-3*x+1, hi)

    def test_t5_positive_certificate(self):
        self.assertEqual(horner_interval([2, 3], F(0), F(1)), (F(3), F(5)))

    def test_t6_unique_root_bracket(self):
        self.assertLess(F(5, 4)**3-2, 0)
        self.assertGreater(F(13, 10)**3-2, 0)

    def test_t7_sturm_quadratic(self):
        p = X**2-2
        self.assertEqual(sturm_variations(p, F(-2))-sturm_variations(p, F(-1)), 1)
        self.assertEqual(sturm_variations(p, F(1))-sturm_variations(p, F(2)), 1)

    def test_t7_sturm_cubic(self):
        p = X**3-X-1
        self.assertEqual(sturm_variations(p, F(1))-sturm_variations(p, F(2)), 1)

    def test_t7_reject_multiple_root(self):
        with self.assertRaises(ValueError):
            sturm_variations((X-1)**2, F(0))

    def test_t8_isolation(self):
        p = X**3-2
        self.assertEqual(sturm_variations(p, F(5, 4))-sturm_variations(p, F(13, 10)), 1)

    def test_t9_zero_numerator(self):
        self.assertTrue(all(ratio_condition(lambda x:0, lambda x:x-1, F(k), "ge") for k in [-3,0,2,5]))
        self.assertFalse(ratio_condition(lambda x:0, lambda x:x-1, F(1), "ge"))

    def test_t10_denominator_interval(self):
        self.assertEqual(horner_interval([1,2], F(0), F(1)), (F(2),F(3)))
        self.assertEqual(horner_interval([3,1], F(0), F(1)), (F(1),F(4)))

    def test_z1(self):
        for k in range(-20,21):
            x=F(k,4)
            self.assertEqual(ratio_condition(lambda t:t-2,lambda t:t+1,x,"ge"),x < -1 or x >= 2)

    def test_z2(self):
        for k in range(-20,21):
            x=F(k,4)
            self.assertEqual(ratio_condition(lambda t:t*t-1,lambda t:t-1,x,"gt"),x > -1 and x != 1)

    def test_z3(self):
        for k in range(-20,21):
            x=F(k,4)
            self.assertEqual(ratio_condition(lambda t:(t-1)**2,lambda t:t+2,x,"le"),x < -2 or x == 1)

    def test_z4(self):
        for k in range(-20,21):
            x=F(k,4)
            self.assertEqual(ratio_condition(lambda t:t*t-2,lambda t:t*t-1,x,"gt"),x*x > 2 or x*x < 1)

    def test_z5(self):
        for k in range(17):
            x=F(k,8)
            self.assertEqual(x**3-x >= 0,x == 0 or x >= 1)

    def test_z6(self):
        self.assertEqual(F(5,4)**3-2,F(-3,64))
        self.assertEqual(F(13,10)**3-2,F(197,1000))

    def test_z7(self):
        self.assertEqual(sturm_variations(X**2-2,F(1))-sturm_variations(X**2-2,F(2)),1)

    def test_z8(self):
        for k in range(-20,21):
            x=F(k,4)
            self.assertGreaterEqual(x*x+1,1)

    def test_z9(self):
        for k in range(-20,21):
            x=F(k,4)
            self.assertEqual(x*x-3*x+2 >= 0,x <= 1 or x >= 2)

    def test_z10(self):
        self.assertEqual(horner_interval([2,3],F(0),F(1)),(F(3),F(5)))

    def test_z11(self):
        a,b=F(3,2),F(2)
        self.assertEqual((a*a-2,b*b-2),(F(1,4),F(2)))

    def test_z12(self):
        for k in range(-20,21):
            x=F(k,4)
            actual=x != 1 and (x*x-1)/(x-1) >= 2
            self.assertEqual(actual,x > 1)

    def test_hole_after_cancellation(self):
        self.assertFalse(ratio_condition(lambda t:t-1,lambda t:t-1,F(1),"ge"))

    def test_interval_dependency_counterexample(self):
        self.assertEqual(interval_add((F(0),F(1)),(F(-1),F(0))),(F(-1),F(1)))


if __name__ == "__main__":
    unittest.main()
