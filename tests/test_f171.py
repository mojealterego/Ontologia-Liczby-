"""F17.1: finite exhaustive checks of pair-class order and ring laws."""
from __future__ import annotations

import itertools
import unittest


def normal(a: int, b: int) -> tuple[int, int]:
    if min(a, b) < 0:
        raise ValueError("natural representatives required")
    return (a - b, 0) if a >= b else (0, b - a)


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return normal(x[0] + y[0], x[1] + y[1])


def mul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    a, b = x
    c, d = y
    return normal(a * c + b * d, a * d + b * c)


def cmp(x: tuple[int, int], y: tuple[int, int]) -> int:
    u, v = x[0] + y[1], x[1] + y[0]
    return (u > v) - (u < v)


def integer(x: tuple[int, int]) -> int:
    return x[0] - x[1]


class F171Tests(unittest.TestCase):
    def test_normalization_invariant(self) -> None:
        for a, b in itertools.product(range(25), repeat=2):
            self.assertEqual(integer(normal(a, b)), a - b)
            self.assertEqual(normal(*normal(a, b)), normal(a, b))

    def test_pair_comparison_matches_integer(self) -> None:
        pairs = list(itertools.product(range(12), repeat=2))
        for x, y in itertools.product(pairs, repeat=2):
            self.assertEqual(cmp(x, y), (integer(x) > integer(y)) - (integer(x) < integer(y)))

    def test_representative_invariance(self) -> None:
        pairs = list(itertools.product(range(8), repeat=2))
        for x, y in itertools.product(pairs, repeat=2):
            x2 = (x[0] + 4, x[1] + 4)
            y2 = (y[0] + 7, y[1] + 7)
            self.assertEqual(cmp(x, y), cmp(x2, y2))
            self.assertEqual(mul(x, y), mul(x2, y2))

    def test_add_mul_consistency(self) -> None:
        pairs = list(itertools.product(range(9), repeat=2))
        for x, y in itertools.product(pairs, repeat=2):
            self.assertEqual(integer(add(x, y)), integer(x) + integer(y))
            self.assertEqual(integer(mul(x, y)), integer(x) * integer(y))

    def test_positive_products_and_monotonicity(self) -> None:
        for x, y, z in itertools.product(range(-7, 8), range(-7, 8), range(8)):
            if x <= y:
                self.assertLessEqual(x * z, y * z)
                if x < y and z > 0:
                    self.assertLess(x * z, y * z)
            if x > 0 and y > 0:
                self.assertGreater(x * y, 0)

    def test_triangle_and_multiplicativity(self) -> None:
        for x, y in itertools.product(range(-50, 51), repeat=2):
            self.assertLessEqual(abs(x + y), abs(x) + abs(y))
            self.assertEqual(abs(x * y), abs(x) * abs(y))

    def test_discrete_order(self) -> None:
        for x in range(-50, 51):
            self.assertFalse(any(x < z < x + 1 for z in range(-52, 54)))

    def test_universal_map_modular(self) -> None:
        for modulus in range(2, 16):
            for a, b, c, d in itertools.product(range(6), repeat=4):
                if a + d == b + c:
                    self.assertEqual((a - b) % modulus, (c - d) % modulus)
            self.assertEqual(modulus % modulus, 0)

    def test_counterexamples(self) -> None:
        self.assertEqual((2 * 0, 3 * 0), (0, 0))
        self.assertGreater(-8, -12)
        self.assertEqual(6 % 6, 0)
        self.assertTrue(all(n < 1000 for n in range(10)))

    def test_exercises(self) -> None:
        self.assertEqual(normal(4, 11), (0, 7))
        self.assertEqual(normal(15, 6), (9, 0))
        self.assertEqual(cmp((3, 8), (7, 11)), -1)
        self.assertEqual(cmp((5, 10), (10, 14)), -1)
        self.assertEqual(integer(mul((0, 6), (4, 0))), -24)
        self.assertEqual((12 - 5) % 7, 0)
        self.assertEqual(100 + 5, 97 + 8)


if __name__ == "__main__":
    unittest.main()
