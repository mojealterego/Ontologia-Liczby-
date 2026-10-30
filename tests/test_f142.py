"""Computational checks for the F14.2 mathematical supplement.

These checks validate finite instances; they do not constitute formal proofs.
Run: python -m unittest discover -s tests -p test_f142.py -v
"""
from __future__ import annotations

import itertools
import unittest
from fractions import Fraction


class UndefinedDivision(ValueError):
    pass


def strict_div(a: Fraction, b: Fraction) -> Fraction:
    if b == 0:
        raise UndefinedDivision("zero denominator")
    return a / b


def inv0(x: int, p: int) -> int:
    if x % p == 0:
        return 0
    return pow(x, p - 2, p)


class F142Tests(unittest.TestCase):
    def test_zero_denominator_is_rejected(self):
        for a in range(-12, 13):
            with self.assertRaises(UndefinedDivision):
                strict_div(Fraction(a), Fraction(0))

    def test_cross_multiplication_with_nonzero_denominators(self):
        for a, b, c, d in itertools.product(range(-3, 4), repeat=4):
            if b and d:
                self.assertEqual(Fraction(a, b) == Fraction(c, d), a * d == b * c)

    def test_cancellation_guard(self):
        for x, y, z in itertools.product(range(-4, 5), repeat=3):
            if y and z:
                self.assertEqual(Fraction(x * z, y * z), Fraction(x, y))

    def test_cancellation_domain_not_preserved(self):
        with self.assertRaises(UndefinedDivision):
            strict_div(Fraction(0), Fraction(0))
        self.assertEqual(strict_div(Fraction(1), Fraction(1)), 1)

    def test_nested_division_guard(self):
        for a, b, c, d in itertools.product(range(-2, 3), repeat=4):
            if b and c and d:
                self.assertEqual(Fraction(a, b) / Fraction(c, d), Fraction(a * d, b * c))

    def test_nested_division_counterexample(self):
        a = b = c = 1
        d = 0
        self.assertEqual(Fraction(a * d, b * c), 0)
        with self.assertRaises(UndefinedDivision):
            strict_div(Fraction(c), Fraction(d))

    def test_zero_totalized_field_inverse(self):
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            for x in range(p):
                i = inv0(x, p)
                self.assertEqual(inv0(i, p), x)
                self.assertEqual(x * (x * i) % p, x)
                self.assertEqual(x * i % p, 0 if x == 0 else 1)

    def test_zero_totalized_division_is_not_field_division(self):
        for a in range(-10, 11):
            self.assertEqual(a * 0, 0)
        self.assertNotEqual(0, 1)

    def test_localization_power_of_two(self):
        for n in range(12):
            self.assertEqual(Fraction(3, 2**n) * (2**n), 3)
        # A fraction 1/3 cannot have a denominator that is a power of two.
        for n in range(30):
            self.assertNotEqual(2**n % 3, 0)

    def test_localization_map_mod_three(self):
        for a in range(-12, 13):
            for n in range(10):
                denominator = pow(2, n, 3)
                self.assertNotEqual(denominator, 0)
                mapped = (a % 3) * pow(denominator, -1, 3) % 3
                self.assertEqual(mapped * denominator % 3, a % 3)

    def test_zero_cannot_be_unit_in_nonzero_ring(self):
        for n in range(2, 30):
            self.assertFalse(any((0 * x) % n == 1 for x in range(n)))

    def test_finite_field_inverse_power_formula(self):
        for p in (3, 5, 7, 11, 13):
            self.assertEqual(inv0(0, p), 0)
            for x in range(1, p):
                self.assertEqual((x * pow(x, p - 2, p)) % p, 1)

    def test_composite_modulus_counterexample(self):
        self.assertEqual(pow(2, 4 - 2, 4), 0)
        self.assertNotEqual(2 * pow(2, 4 - 2, 4) % 4, 1)

    def test_perturbation_bound_exhaustive(self):
        for a in range(-4, 5):
            for ap in range(-4, 5):
                for b in range(-5, 6):
                    if not b:
                        continue
                    for bp in range(-5, 6):
                        if abs(bp - b) * 2 <= abs(b):
                            self.assertNotEqual(bp, 0)
                            lhs = abs(Fraction(a, b) - Fraction(ap, bp))
                            rhs = Fraction(abs(a - ap), abs(b)) + Fraction(2 * abs(ap) * abs(b - bp), b * b)
                            self.assertLessEqual(lhs, rhs)

    def test_exercises(self):
        self.assertEqual(Fraction(6, 2) / Fraction(3, 5), 5)
        self.assertEqual(Fraction(3, 8) * 8, 3)
        self.assertEqual([inv0(x, 5) for x in range(5)], [0, 1, 3, 2, 4])
        self.assertEqual(inv0(3, 7), 5)
        self.assertEqual(abs(Fraction(1, 100) ** -1 - Fraction(1, 200) ** -1), 100)

    def test_fraction_field_arithmetic(self):
        for a, b, s, t in itertools.product(range(-3, 4), repeat=4):
            if s and t:
                self.assertEqual(Fraction(a, s) + Fraction(b, t), Fraction(a*t+b*s, s*t))
                self.assertEqual(Fraction(a, s) * Fraction(b, t), Fraction(a*b, s*t))


if __name__ == "__main__":
    unittest.main()
