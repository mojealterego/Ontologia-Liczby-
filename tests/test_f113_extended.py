"""Finite checks for the F11.3 extension (weighted and interval certificates)."""
import unittest
from itertools import product


def weighted(values: tuple[int, ...], modulus: int) -> int:
    return sum((i + 1) * x for i, x in enumerate(values)) % modulus


class F113ExtendedTests(unittest.TestCase):
    def test_weighted_transposition_formula(self):
        for xs in product(range(-3, 4), repeat=4):
            for i in range(4):
                for j in range(i + 1, 4):
                    ys = list(xs)
                    ys[i], ys[j] = ys[j], ys[i]
                    for modulus in (5, 7, 11):
                        delta = (weighted(tuple(ys), modulus) - weighted(xs, modulus)) % modulus
                        self.assertEqual(delta, ((i - j) * (xs[j] - xs[i])) % modulus)

    def test_prime_detection_guarantee(self):
        for prime in (5, 7, 11):
            for i in range(prime):
                for j in range(i + 1, prime):
                    for x in range(prime):
                        for y in range(prime):
                            if x != y:
                                self.assertNotEqual(((i - j) * (y - x)) % prime, 0)

    def test_interval_bound(self):
        bounds = ((2, 3), (-1, 1), (5, 8))
        for values in product(*(range(lo, hi + 1) for lo, hi in bounds)):
            self.assertTrue(6 <= sum(values) <= 12)

    def test_modular_interval_uniqueness(self):
        for modulus in range(2, 20):
            for lo in range(-12, 12):
                hi = lo + modulus - 1
                for x in range(lo, hi + 1):
                    for y in range(lo, hi + 1):
                        if x % modulus == y % modulus:
                            self.assertEqual(x, y)

    def test_prefix_monotonicity_equivalence(self):
        for xs in product(range(-2, 3), repeat=4):
            prefixes = [0]
            for x in xs:
                prefixes.append(prefixes[-1] + x)
            self.assertEqual(all(a <= b for a, b in zip(prefixes, prefixes[1:])), all(x >= 0 for x in xs))

    def test_solved_examples(self):
        self.assertEqual(weighted((4, 9), 11), 0)
        self.assertEqual(weighted((9, 4), 11), 6)
        self.assertEqual(weighted((2, 7), 5), weighted((7, 2), 5))
        self.assertEqual((0, 4, -3, 7), tuple(sum((4, -7, 10)[:i]) for i in range(4)))
        self.assertEqual((0, 2, 2, 7), tuple(sum((2, 0, 5)[:i]) for i in range(4)))
        self.assertEqual((0, 2, 1, 6), tuple(sum((2, -1, 5)[:i]) for i in range(4)))


if __name__ == '__main__':
    unittest.main()
