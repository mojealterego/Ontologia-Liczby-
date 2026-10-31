"""Finite checks for Tom I, F16.1: exact fractions, height and modular reconstruction."""
from fractions import Fraction
from math import gcd, lcm
import unittest


def height(q: Fraction) -> int:
    return max(abs(q.numerator), q.denominator)


def canonical_denominator(q: Fraction) -> int:
    return q.denominator


def phi(n: int) -> int:
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


class TestF161(unittest.TestCase):
    def setUp(self):
        self.qs = [Fraction(a, b) for a in range(-8, 9) for b in range(1, 9)]

    def test_t1_minimal_denominator(self):
        for q in self.qs:
            for d in range(1, 31):
                if (q*d).denominator == 1:
                    self.assertEqual(d % canonical_denominator(q), 0)

    def test_t2_denominator_of_sum(self):
        for q in self.qs:
            for r in self.qs:
                self.assertEqual(lcm(q.denominator, r.denominator) % (q+r).denominator, 0)

    def test_t3_coprime_denominators(self):
        for q in self.qs:
            for r in self.qs:
                if gcd(q.denominator, r.denominator) == 1:
                    self.assertEqual((q+r).denominator, q.denominator*r.denominator)

    def test_t4_denominator_of_product(self):
        for q in self.qs:
            for r in self.qs:
                self.assertEqual((q.denominator*r.denominator) % (q*r).denominator, 0)

    def test_t5_t6_height_symmetries(self):
        for q in self.qs:
            self.assertEqual(height(q), height(-q))
            if q:
                self.assertEqual(height(q), height(1/q))

    def test_t7_t8_height_bounds(self):
        for q in self.qs:
            for r in self.qs:
                self.assertLessEqual(height(q*r), height(q)*height(r))
                self.assertLessEqual(height(q+r), 2*height(q)*height(r))

    def test_t9_finiteness(self):
        for N in range(1, 12):
            ball = {Fraction(a,b) for a in range(-N,N+1) for b in range(1,N+1) if height(Fraction(a,b)) <= N}
            self.assertLessEqual(len(ball), (2*N+1)*N)

    def test_t10_totient_count(self):
        for N in range(1, 18):
            vals = {Fraction(a,b) for a in range(0,N+1) for b in range(1,N+1) if 0 <= Fraction(a,b) <= 1 and height(Fraction(a,b)) <= N}
            self.assertEqual(len(vals), 1+sum(phi(b) for b in range(1,N+1)))

    def test_t11_unique_modular_reconstruction(self):
        for A in range(1,5):
            for B in range(1,5):
                for M in range(2*A*B+1, 2*A*B+7):
                    codes = {}
                    for b in range(1,B+1):
                        if gcd(b,M)!=1:
                            continue
                        for a in range(-A,A+1):
                            q = Fraction(a,b)
                            if q.numerator != a or q.denominator != b:
                                continue
                            code = (a*pow(b,-1,M))%M
                            self.assertNotIn(code, codes, (A,B,M,q,codes.get(code)))
                            codes[code]=q

    def test_t12_representation_invariance(self):
        for M in range(2,30):
            for q in self.qs:
                b = q.denominator
                if gcd(b,M)!=1:
                    continue
                for t in range(1,8):
                    d = b*t
                    if gcd(d,M)==1:
                        self.assertEqual(q.numerator*pow(b,-1,M)%M,(q.numerator*t)*pow(d,-1,M)%M)

    def test_counterexamples(self):
        self.assertEqual(height(Fraction(1,100)),100)
        self.assertEqual(Fraction(1,6)+Fraction(1,6),Fraction(1,3))
        self.assertEqual(height(Fraction(2,3)*Fraction(3,2)),1)
        self.assertEqual((2*pow(1,-1,5))%5,((-1)*pow(2,-1,5))%5)

    def test_solved_exercises(self):
        self.assertEqual(Fraction(-42,56).denominator,4)
        self.assertEqual(height(Fraction(-42,56)),4)
        self.assertEqual((Fraction(1,4)+Fraction(1,9)).denominator,36)
        self.assertEqual((Fraction(1,6)+Fraction(1,6)).denominator,3)
        self.assertEqual(height(Fraction(-3,7)**-1),7)
        self.assertEqual((3*pow(4,-1,11))%11,9)
        self.assertEqual(Fraction(18,30),Fraction(3,5))


if __name__ == '__main__':
    unittest.main()
