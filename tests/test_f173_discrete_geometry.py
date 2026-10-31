"""Finite, reproducible checks for the F17.3 discrete-geometry supplement.

These checks exercise examples and finite instances; they are not proofs of
universal statements or substitutes for editorial review.
"""
from __future__ import annotations

import itertools
import math
import unittest
from fractions import Fraction


def projection(x: int, lo: int, hi: int) -> int:
    if lo > hi:
        raise ValueError("empty integer interval")
    return min(hi, max(lo, x))


def nearest_integers(q: Fraction) -> list[int]:
    lo = q.numerator // q.denominator
    hi = -((-q.numerator) // q.denominator)
    options = sorted({lo, hi})
    best = min(abs(q - n) for n in options)
    return [n for n in options if abs(q - n) == best]


class F173DiscreteGeometryTests(unittest.TestCase):
    def test_t1_interval_cardinality(self) -> None:
        for a in range(-25, 26):
            for b in range(a, 26):
                self.assertEqual(len(list(range(a, b + 1))), b - a + 1)

    def test_t2_triangle_inequality(self) -> None:
        for a, b, c in itertools.product(range(-8, 9), repeat=3):
            self.assertLessEqual(abs(a - c), abs(a - b) + abs(b - c))

    def test_t3_reverse_triangle(self) -> None:
        for a, b, c in itertools.product(range(-8, 9), repeat=3):
            self.assertLessEqual(abs(abs(a - c) - abs(b - c)), abs(a - b))

    def test_t4_path_lower_bound(self) -> None:
        for a, b in itertools.product(range(-20, 21), repeat=2):
            path = list(range(a, b + 1)) if a <= b else list(range(a, b - 1, -1))
            self.assertEqual(len(path) - 1, abs(a - b))

    def test_t5_triangle_equality(self) -> None:
        for a, b, c in itertools.product(range(-8, 9), repeat=3):
            lhs = abs(a - c) == abs(a - b) + abs(b - c)
            rhs = (a <= b <= c) or (c <= b <= a)
            self.assertEqual(lhs, rhs)

    def test_t6_unique_projection(self) -> None:
        for lo in range(-6, 7):
            for hi in range(lo, 7):
                for x in range(-12, 13):
                    p = projection(x, lo, hi)
                    minimum = min(abs(x - y) for y in range(lo, hi + 1))
                    minimizers = [y for y in range(lo, hi + 1) if abs(x - y) == minimum]
                    self.assertEqual(minimizers, [p])

    def test_t7_projection_nonexpansive(self) -> None:
        for lo, hi in [(-4, 3), (0, 0), (-10, -2), (4, 11)]:
            for x, y in itertools.product(range(-20, 21), repeat=2):
                self.assertLessEqual(abs(projection(x, lo, hi) - projection(y, lo, hi)), abs(x - y))

    def test_t8_isometry(self) -> None:
        for t in range(-5, 6):
            for x, y in itertools.product(range(-10, 11), repeat=2):
                self.assertEqual(abs((x + t) - (y + t)), abs(x - y))
                self.assertEqual(abs((t - x) - (t - y)), abs(x - y))

    def test_t9_isolated_points(self) -> None:
        for n in range(-100, 101):
            self.assertEqual([k for k in range(n - 2, n + 3) if abs(k - n) < 1], [n])

    def test_t14_nearest_rationals(self) -> None:
        for den in range(1, 16):
            for num in range(-40, 41):
                q = Fraction(num, den)
                minima = nearest_integers(q)
                brute = min(abs(q - n) for n in range(-50, 51))
                self.assertEqual([n for n in range(-50, 51) if abs(q - n) == brute], minima)

    def test_t15_rational_interval(self) -> None:
        for den1 in range(1, 5):
            for den2 in range(1, 5):
                for num1 in range(-7, 8):
                    for num2 in range(-7, 8):
                        lo, hi = Fraction(num1, den1), Fraction(num2, den2)
                        if lo > hi:
                            continue
                        floor_hi = hi.numerator // hi.denominator
                        ceil_lo = -((-lo.numerator) // lo.denominator)
                        expected = max(0, floor_hi - ceil_lo + 1)
                        actual = sum(lo <= n <= hi for n in range(-20, 21))
                        self.assertEqual(actual, expected)

    def test_t16_absolute_value_ball(self) -> None:
        for a in range(-12, 13):
            for radius in range(0, 15):
                solutions = [x for x in range(-50, 51) if abs(x - a) <= radius]
                self.assertEqual(solutions, list(range(a - radius, a + radius + 1)))

    def test_t18_closed_ball(self) -> None:
        for a in range(-10, 11):
            for den in range(1, 7):
                for num in range(0, 40):
                    radius = Fraction(num, den)
                    count = sum(abs(x - a) <= radius for x in range(-60, 61))
                    self.assertEqual(count, 2 * (num // den) + 1)

    def test_counterexamples(self) -> None:
        self.assertEqual(len(list(range(-2, 3))), 5)
        self.assertEqual(abs(Fraction(7, 2) - 3), abs(Fraction(7, 2) - 4))
        self.assertEqual(min(abs(0 - n) for n in [-1, 1]), 1)
        self.assertEqual([n for n in range(10) if min(abs(n - 0), 10 - abs(n - 0)) == 1], [1, 9])

    def test_solved_exercises(self) -> None:
        self.assertEqual(len(list(range(-17, 24))), 41)
        self.assertEqual([x for x in range(-30, 31) if abs(2 * x + 1) < 8], list(range(-4, 4)))
        self.assertEqual([x for x in range(-20, 21) if abs(x + 2) + abs(x - 5) == 9], [-3, 6])
        self.assertEqual(nearest_integers(Fraction(-13, 4)), [-3])
        self.assertEqual(nearest_integers(Fraction(-9, 2)), [-5, -4])
        self.assertEqual(len([(a, b) for a in range(4) for b in range(-2, 3)]), 20)


if __name__ == "__main__":
    unittest.main()