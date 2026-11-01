"""Exact arithmetic verification for Ontologia Liczby F23.1 supplement.

Finite checks are evidence for examples, not formal proofs of all theorems.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd
import unittest


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """Return nonnegative gcd and Bézout coefficients (g,u,v)."""
    old_r, r = a, b
    old_u, u = 1, 0
    old_v, v = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_u, u = u, old_u - q * u
        old_v, v = v, old_v - q * v
    if old_r < 0:
        return -old_r, -old_u, -old_v
    return old_r, old_u, old_v


def modular_solutions(a: int, d: int, n: int) -> list[int]:
    if n < 2:
        raise ValueError("n must be >= 2")
    return [x for x in range(n) if (a * x - d) % n == 0]


def certificate_solution(a: int, d: int, n: int) -> int | None:
    if n < 2:
        raise ValueError("n must be >= 2")
    g, u, v = egcd(a, n)
    assert u * a + v * n == g
    if d % g:
        return None
    return (u * (d // g)) % n


class LinearFibersTests(unittest.TestCase):
    def test_t1_fiber_coset_modular_exhaustive(self) -> None:
        for n in range(2, 21):
            for a in range(n):
                ann = set(modular_solutions(a, 0, n))
                for d in range(n):
                    sols = modular_solutions(a, d, n)
                    if sols:
                        x0 = sols[0]
                        self.assertEqual(set(sols), {(x0 + h) % n for h in ann})

    def test_t2_image_membership(self) -> None:
        for n in range(2, 21):
            for a in range(n):
                image = {(a * x) % n for x in range(n)}
                for d in range(n):
                    self.assertEqual(bool(modular_solutions(a, d, n)), d in image)

    def test_t3_injective_iff_ann_trivial(self) -> None:
        for n in range(2, 40):
            for a in range(n):
                injective = len({(a * x) % n for x in range(n)}) == n
                self.assertEqual(injective, modular_solutions(a, 0, n) == [0])

    def test_t4_surjective_iff_unit(self) -> None:
        for n in range(2, 40):
            for a in range(n):
                surjective = len({a * x % n for x in range(n)}) == n
                self.assertEqual(surjective, gcd(a, n) == 1)

    def test_t5_integer_solvability(self) -> None:
        for a in range(-20, 21):
            for d in range(-20, 21):
                xs = [x for x in range(-20, 21) if a * x == d]
                if a:
                    self.assertEqual(bool(xs), d % a == 0 and -20 <= d // a <= 20)
                else:
                    self.assertEqual(bool(xs), d == 0)

    def test_t6_modular_classification(self) -> None:
        for n in range(2, 40):
            for a in range(-20, 21):
                g = gcd(a, n)
                for d in range(-8, 9):
                    xs = modular_solutions(a, d, n)
                    self.assertEqual(len(xs), g if d % g == 0 else 0)
                    if xs:
                        self.assertEqual({x % (n // g) for x in xs}, {xs[0] % (n // g)})

    def test_t7_bezout_certificates(self) -> None:
        for n in range(2, 60):
            for a in range(-25, 26):
                g, u, v = egcd(a, n)
                self.assertEqual(u * a + v * n, g)
                self.assertEqual(g, gcd(a, n))
                for d in [-30, -1, 0, 1, 18, 30]:
                    x = certificate_solution(a, d, n)
                    self.assertEqual(x is not None, d % g == 0)
                    if x is not None:
                        self.assertEqual((a * x - d) % n, 0)

    def test_t8_unit_inverse(self) -> None:
        for n in range(2, 60):
            for a in range(n):
                sols = modular_solutions(a, 1, n)
                self.assertEqual(len(sols), 1 if gcd(a, n) == 1 else 0)

    def test_t9_crt_count(self) -> None:
        for n in range(2, 14):
            for m in range(2, 14):
                if gcd(n, m) != 1:
                    continue
                for a in range(-4, 5):
                    for d in range(-3, 4):
                        left = modular_solutions(a, d, n)
                        right = modular_solutions(a, d, m)
                        joint = modular_solutions(a, d, n * m)
                        self.assertEqual(len(joint), len(left) * len(right))

    def test_t10_perturbation_identity_exact(self) -> None:
        for a in [-7, -3, -1, 1, 2, 5]:
            for d in [-11, -1, 0, 3, 10]:
                for da in [Fraction(-1, 3), Fraction(0), Fraction(1, 4)]:
                    for dd in [Fraction(-1, 7), Fraction(0), Fraction(1, 5)]:
                        A, D = Fraction(a), Fraction(d)
                        x = D / A
                        xp = (D + dd) / (A + da)
                        self.assertEqual(xp - x, (A * dd - D * da) / (A * (A + da)))
                        eta = abs(da / A)
                        self.assertLess(eta, 1)
                        bound = (abs(dd) + abs(x) * abs(da)) / ((1 - eta) * abs(A))
                        self.assertLessEqual(abs(xp - x), bound)

    def test_t11_residual_error(self) -> None:
        for a in [-9, -2, 1, 3, 10]:
            for d in [-12, 0, 7]:
                x = Fraction(d, a)
                for error in [Fraction(-1, 100), Fraction(0), Fraction(3, 7)]:
                    xt = x + error
                    r = a * xt - d
                    self.assertEqual(xt - x, r / a)

    def test_t12_fraction_field(self) -> None:
        for a in range(-20, 21):
            if a == 0:
                continue
            for d in range(-20, 21):
                q = Fraction(d, a)
                self.assertEqual(q.denominator == 1, d % a == 0)

    def test_k1_two_solutions(self) -> None:
        self.assertEqual(modular_solutions(2, 2, 6), [1, 4])

    def test_k2_integer_vs_rational(self) -> None:
        self.assertNotEqual(Fraction(1, 2).denominator, 1)

    def test_k3_inconsistent_congruence(self) -> None:
        self.assertEqual(modular_solutions(6, 5, 15), [])

    def test_k4_small_residual_large_error(self) -> None:
        a = Fraction(1, 10**12)
        r = Fraction(1, 10**6)
        self.assertEqual(r / a, 10**6)

    def test_k5_restricted_domain(self) -> None:
        self.assertFalse(Fraction(2) in [Fraction(0), Fraction(1)])

    def test_k6_four_solutions(self) -> None:
        self.assertEqual(modular_solutions(4, 4, 8), [1, 3, 5, 7])

    def test_z3(self) -> None:
        self.assertEqual(modular_solutions(6, 9, 15), [4, 9, 14])

    def test_z4(self) -> None:
        self.assertEqual(modular_solutions(8, 3, 12), [])

    def test_z5_z6(self) -> None:
        self.assertEqual(7 * 15 - 26 * 4, 1)
        self.assertEqual(modular_solutions(7, 5, 26), [23])

    def test_z8(self) -> None:
        self.assertEqual(modular_solutions(3, 6, 35), [2])

    def test_z9(self) -> None:
        self.assertEqual(modular_solutions(6, 6, 72), [1, 13, 25, 37, 49, 61])

    def test_z10(self) -> None:
        x = Fraction(6, 2)
        xp = Fraction(7, 1) / Fraction(5, 2)
        self.assertEqual(xp - x, Fraction(-1, 5))

    def test_z11(self) -> None:
        xt = Fraction(7, 3) + Fraction(1, 300)
        self.assertEqual(3 * xt - 7, Fraction(1, 100))

    def test_reject_invalid_modulus(self) -> None:
        with self.assertRaises(ValueError):
            modular_solutions(2, 3, 1)
        with self.assertRaises(ValueError):
            certificate_solution(2, 3, 0)


if __name__ == "__main__":
    unittest.main()
