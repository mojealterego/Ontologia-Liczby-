"""Exact arithmetic regression tests for F14.4; standard library only."""
import math
import unittest
from fractions import Fraction


def continued_fraction(x: Fraction) -> list[int]:
    if not isinstance(x, Fraction):
        raise TypeError("expected Fraction")
    a, b = x.numerator, x.denominator
    terms = []
    while True:
        q, r = divmod(a, b)
        terms.append(q)
        if r == 0:
            return terms
        a, b = b, r


def convergents(terms: list[int]) -> list[tuple[int, int]]:
    if not terms or any(a < 1 for a in terms[1:]):
        raise ValueError("invalid continued fraction")
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    out = []
    for a in terms:
        p, q = a * pm1 + pm2, a * qm1 + qm2
        out.append((p, q))
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    return out


class TestF144(unittest.TestCase):
    def test_exact_reconstruction_and_canonical(self):
        for b in range(1, 40):
            for a in range(-80, 81):
                x = Fraction(a, b)
                terms = continued_fraction(x)
                cv = convergents(terms)
                self.assertEqual(Fraction(*cv[-1]), x)
                self.assertTrue(len(terms) == 1 or terms[-1] >= 2)

    def test_unimodular_and_coprime(self):
        for b in range(1, 26):
            for a in range(-50, 51):
                cv = convergents(continued_fraction(Fraction(a, b)))
                for n, (p, q) in enumerate(cv):
                    self.assertGreater(q, 0)
                    self.assertEqual(math.gcd(abs(p), q), 1)
                    if n:
                        pp, qq = cv[n-1]
                        self.assertEqual(p * qq - pp * q, (-1) ** (n+1))

    def test_error_sign_and_bound(self):
        for b in range(2, 35):
            for a in range(-60, 61):
                x = Fraction(a, b)
                cv = convergents(continued_fraction(x))
                for n in range(len(cv)-1):
                    p, q = cv[n]
                    qnext = cv[n+1][1]
                    diff = x - Fraction(p, q)
                    self.assertGreater(diff * ((-1) ** n), 0)
                    self.assertLessEqual(abs(diff), Fraction(1, q * qnext))
                    if n+1 == len(cv)-1:
                        self.assertEqual(abs(diff), Fraction(1, q * qnext))
                    else:
                        self.assertLess(abs(diff), Fraction(1, q * qnext))

    def test_denominator_growth(self):
        for b in range(1, 25):
            for a in range(-40, 41):
                cv = convergents(continued_fraction(Fraction(a, b)))
                for n in range(1, len(cv)):
                    self.assertGreaterEqual(cv[n][1], cv[n-1][1])
                    if n >= 2:
                        self.assertGreater(cv[n][1], cv[n-1][1])

    def test_lattice_gcd_invariant(self):
        cv = convergents([4, 2, 6, 7])
        for n in range(1, len(cv)):
            p, q = cv[n]
            pp, qq = cv[n-1]
            for u in range(-5, 6):
                for v in range(-5, 6):
                    A, B = u*p+v*pp, u*q+v*qq
                    self.assertEqual(math.gcd(abs(A), abs(B)), math.gcd(abs(u), abs(v)))

    def test_worked_examples(self):
        self.assertEqual(continued_fraction(Fraction(415, 93)), [4,2,6,7])
        self.assertEqual(convergents([4,2,6,7]), [(4,1),(9,2),(58,13),(415,93)])
        self.assertEqual(continued_fraction(Fraction(-7,3)), [-3,1,2])
        self.assertEqual(continued_fraction(Fraction(5,3)), [1,1,2])
        self.assertEqual(Fraction(415,93)-Fraction(58,13), Fraction(1,1209))
        self.assertEqual(abs(Fraction(7,5)-Fraction(3,2)), Fraction(1,10))

    def test_tail_identity(self):
        for b in range(2, 24):
            for a in range(-35, 36):
                x = Fraction(a, b)
                terms = continued_fraction(x)
                cv = convergents(terms)
                for n in range(len(cv) - 1):
                    tail = Fraction(*convergents(terms[n+1:])[-1])
                    p, q = cv[n]
                    pp, qq = cv[n-1] if n else (1, 0)
                    self.assertEqual(x, Fraction(p*tail+pp, q*tail+qq))

    def test_adjacent_convergent_distance(self):
        for b in range(1, 25):
            for a in range(-35, 36):
                cv = convergents(continued_fraction(Fraction(a, b)))
                for n in range(1, len(cv)):
                    p, q = cv[n]
                    pp, qq = cv[n-1]
                    self.assertEqual(abs(Fraction(p,q)-Fraction(pp,qq)), Fraction(1,q*qq))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            continued_fraction(0.5)
        for terms in ([], [0,0], [1,-1]):
            with self.assertRaises(ValueError):
                convergents(terms)


if __name__ == '__main__':
    unittest.main()
