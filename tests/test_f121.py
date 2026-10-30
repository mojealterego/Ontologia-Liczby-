"""Finite-model regression checks for Tom I / F12.1.

These checks do not replace the mathematical proofs in the manuscript.
"""
from itertools import product
import unittest


def equiv(x: tuple[int, int], y: tuple[int, int]) -> bool:
    return x[0] + y[1] == x[1] + y[0]


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[1], x[1] + y[0]


def value(x: tuple[int, int]) -> int:
    return x[0] - x[1]


class F121Tests(unittest.TestCase):
    def test_partial_subtraction_domain_and_value(self):
        for a, b in product(range(30), repeat=2):
            solutions = [c for c in range(30) if b + c == a]
            self.assertEqual(len(solutions), int(a >= b))
            if solutions:
                self.assertEqual(solutions[0], a - b)

    def test_translation_invariance(self):
        for a, b, t in product(range(9), repeat=3):
            self.assertEqual(a <= b, a + t <= b + t)
            if a <= b:
                self.assertEqual(b - a, (b + t) - (a + t))

    def test_equivalence_iff_integer_difference(self):
        pairs = list(product(range(7), repeat=2))
        for x in pairs:
            for y in pairs:
                self.assertEqual(equiv(x, y), value(x) == value(y))

    def test_equivalence_transitivity(self):
        pairs = list(product(range(4), repeat=2))
        for x, y, z in product(pairs, repeat=3):
            if equiv(x, y) and equiv(y, z):
                self.assertTrue(equiv(x, z))

    def test_addition_respects_representatives(self):
        pairs = list(product(range(5), repeat=2))
        for x, y, z in product(pairs, repeat=3):
            if equiv(x, y):
                self.assertTrue(equiv(add(x, z), add(y, z)))

    def test_group_inverse(self):
        for x in product(range(20), repeat=2):
            self.assertTrue(equiv(add(x, (x[1], x[0])), (0, 0)))

    def test_injection_and_positive_cone(self):
        for a, b in product(range(30), repeat=2):
            self.assertEqual(equiv((a, 0), (b, 0)), a == b)
            self.assertEqual(value((a, b)) >= 0, a >= b)

    def test_subtraction_of_classes(self):
        for x, y in product(product(range(7), repeat=2), repeat=2):
            self.assertEqual(value(sub(x, y)), value(x) - value(y))

    def test_telescoping(self):
        for xs in product(range(-2, 3), repeat=4):
            self.assertEqual(sum(xs[i] - xs[i + 1] for i in range(3)), xs[0] - xs[-1])

    def test_universal_extension_to_modular_group(self):
        for modulus in range(2, 10):
            for generator in range(modulus):
                for a, b in product(range(8), repeat=2):
                    extended = ((a - b) * generator) % modulus
                    self.assertEqual(extended, (a * generator - b * generator) % modulus)
                    self.assertEqual(extended, (value((a, b)) * generator) % modulus)

    def test_noncancellative_counterexample(self):
        self.assertEqual(max(1, 1), max(1, 0))
        self.assertNotEqual(1, 0)

    def test_solved_exercises(self):
        self.assertTrue(equiv((4, 1), (7, 4)))
        self.assertEqual(value((2, 7)), -5)
        self.assertEqual(value(add((8, 3), (1, 4))), 2)
        self.assertEqual(value(sub((3, 8), (4, 6))), -3)
        self.assertEqual(value(add(add((3, 7), (7, 10)), (10, 2))), 1)
        self.assertTrue(equiv((5, 2), (11, 8)))
        self.assertEqual(value(sub((15, 9), (4, 12))), 14)


if __name__ == "__main__":
    unittest.main()
