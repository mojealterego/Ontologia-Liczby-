"""Exact regression checks for Ontologia Liczby F22.3 supplement.

Finite examples and polynomial certificates; not a formal proof of all statements.
"""
from __future__ import annotations

import math
import unittest
from functools import reduce
from sympy import Poly, symbols, factor_list, gcd, primerange, QQ, ZZ

X = symbols("X")


def content(coeffs: list[int]) -> int:
    """Positive gcd of coefficients; input must contain a nonzero entry."""
    if not any(coeffs):
        raise ValueError("zero polynomial has no positive content here")
    return reduce(math.gcd, map(abs, coeffs), 0)


def eisenstein(coeffs_desc: list[int], prime: int) -> bool:
    """Leading-first integer coefficients; positive-degree polynomial."""
    if len(coeffs_desc) < 2:
        raise ValueError("invalid input")
    if prime not in list(primerange(2, prime + 1)):
        raise ValueError("prime required")
    return (coeffs_desc[0] % prime != 0
            and all(c % prime == 0 for c in coeffs_desc[1:])
            and coeffs_desc[-1] % (prime * prime) != 0)


class TestF223Certificates(unittest.TestCase):
    def test_01_content(self):
        self.assertEqual(content([6, 9, 3]), 3)

    def test_02_content_product(self):
        f, g = Poly(2*X + 2, X), Poly(3*X - 3, X)
        self.assertEqual(content((f*g).all_coeffs()), 6)

    def test_03_gauss_grid(self):
        for a in range(-3, 4):
            for b in range(-3, 4):
                if a == b == 0:
                    continue
                f = Poly(a*X + b, X, domain=ZZ)
                g = Poly((b+1)*X + (a+2), X, domain=ZZ)
                if not g.is_zero:
                    self.assertEqual(content((f*g).all_coeffs()),
                                     content(f.all_coeffs()) * content(g.all_coeffs()))

    def test_04_eisenstein_fifth(self):
        self.assertTrue(eisenstein([1, 0, 0, 0, 10, 5], 5))

    def test_05_eisenstein_cubic(self):
        self.assertTrue(eisenstein([1, 0, 0, -2], 2))

    def test_06_eisenstein_negative(self):
        self.assertFalse(eisenstein([1, 0, 0, 0, 4], 2))

    def test_07_shifted_eisenstein(self):
        f = Poly((X+1)**4 + 1, X, domain=ZZ)
        self.assertEqual(f.all_coeffs(), [1, 4, 6, 4, 2])
        self.assertTrue(eisenstein(f.all_coeffs(), 2))

    def test_08_quartic_q_irreducible(self):
        self.assertTrue(Poly(X**4 + 1, X, domain=QQ).is_irreducible)

    def test_09_converse_mod2_false(self):
        f = Poly(X**4 + 1, X, modulus=2)
        self.assertFalse(f.is_irreducible)
        self.assertEqual(factor_list(f)[1][0][1], 4)

    def test_10_degree_drop(self):
        self.assertEqual(Poly(2*X**2+X+1, X, modulus=2).degree(), 1)

    def test_11_irreducible_cubic_mod2(self):
        self.assertTrue(Poly(X**3 + X + 1, X, modulus=2).is_irreducible)

    def test_12_irreducible_quadratic_mod3(self):
        self.assertTrue(Poly(X**2 + 1, X, modulus=3).is_irreducible)

    def test_13_gcd_derivative(self):
        f = Poly((X-1)**3*(X+2)**2, X, domain=QQ)
        self.assertEqual(gcd(f, f.diff()).monic().as_expr(), ((X-1)**2*(X+2)).expand())

    def test_14_squarefree_quotient(self):
        f = Poly((X-1)**3*(X+2)**2, X, domain=QQ)
        q = f.exquo(gcd(f, f.diff()))
        self.assertEqual(q.as_expr().expand(), ((X-1)*(X+2)).expand())

    def test_15_derivative_zero_char3(self):
        f = Poly(X**6 + X**3 + 1, X, modulus=3)
        self.assertTrue(f.diff().is_zero)

    def test_16_frobenius_cube(self):
        self.assertTrue(Poly(X**6+X**3+1-(X**2+X+1)**3, X, modulus=3).is_zero)

    def test_17_linear_part_mod5(self):
        f = Poly((X-1)**2*(X-3)*(X**2+2), X, modulus=5)
        xp = Poly(X**5-X, X, modulus=5)
        self.assertEqual(gcd(f, xp).monic(), Poly((X-1)*(X-3), X, modulus=5).monic())

    def test_18_no_root_quadratic_mod5(self):
        self.assertTrue(all((a*a+2) % 5 for a in range(5)))

    def test_19_bezout(self):
        f, g = Poly(X, X, domain=QQ), Poly(X-1, X, domain=QQ)
        self.assertEqual(f-g, Poly(1, X, domain=QQ))

    def test_20_zero_divisors(self):
        self.assertEqual([a for a in range(8) if a*(a-2) % 8 == 0], [0,2,4,6])

    def test_21_factorization_not_irreducibility(self):
        f = Poly(X**4-1, X, domain=QQ)
        self.assertEqual(f, Poly(X**2-1, X, domain=QQ)*Poly(X**2+1, X, domain=QQ))
        self.assertFalse(Poly(X**2-1, X).is_irreducible)

    def test_22_quartic_mod2(self):
        f = Poly(X**4+X+1, X, modulus=2)
        self.assertTrue(f.is_irreducible)
        self.assertEqual(f.rem(Poly(X**2+X+1, X, modulus=2)), Poly(1, X, modulus=2))

    def test_23_quartic_over_q(self):
        self.assertTrue(Poly(X**4+X+1, X, domain=QQ).is_irreducible)

    def test_24_identity_grid(self):
        for a in range(-4, 5):
            for b in range(-4, 5):
                self.assertEqual(Poly(X**2-(a+b)*X+a*b, X),
                                 Poly(X-a, X)*Poly(X-b, X))


if __name__ == "__main__":
    unittest.main()
