"""Reproducible finite-instance checks for F13.1.

These checks do not constitute a formal proof of all universally quantified theorems.
"""
from __future__ import annotations

import math
import unittest
from itertools import product


def table(m: int, n: int) -> list[list[int]]:
    if m < 0 or n < 0:
        raise ValueError("dimensions must be nonnegative")
    return [[i * j for j in range(n + 1)] for i in range(m + 1)]


def certify(u: list[list[int]]) -> bool:
    if not u or not u[0]:
        return False
    width = len(u[0])
    if any(len(row) != width for row in u):
        return False
    return all(row[0] == 0 and all(row[j + 1] - row[j] == i
                                   for j in range(width - 1))
               for i, row in enumerate(u))


def period(a: int, q: int) -> int:
    if a < 0 or q < 2:
        raise ValueError("a >= 0 and q >= 2 are required")
    return q // math.gcd(a, q)


class TestF131(unittest.TestCase):
    def test_t1_additive_maps(self) -> None:
        for c in range(21):
            f = lambda x: c * x
            for a, b in product(range(31), repeat=2):
                self.assertEqual(f(a + b), f(a) + f(b))
                self.assertEqual(f(a), a * f(1))

    def test_t2_certificate_all_small_tables(self) -> None:
        for m, n in product(range(10), repeat=2):
            t = table(m, n)
            self.assertTrue(certify(t))
            self.assertEqual(t[-1][-1], m * n)

    def test_t2_single_field_corruption(self) -> None:
        for m, n in product(range(1, 6), repeat=2):
            for i, j in product(range(m + 1), range(n + 1)):
                t = table(m, n)
                t[i][j] += 1
                self.assertFalse(certify(t), (m, n, i, j))

    def test_t3_t4_row_differences_and_order(self) -> None:
        for a in range(20):
            r = [a * j for j in range(40)]
            self.assertEqual([r[j + 1] - r[j] for j in range(39)], [a] * 39)
            self.assertEqual(len(set(r)), 40 if a > 0 else 1)

    def test_t5_cancellation_and_zero_product(self) -> None:
        for a, b, c in product(range(16), repeat=3):
            if a > 0 and a * b == a * c:
                self.assertEqual(b, c)
            if a * b == 0:
                self.assertTrue(a == 0 or b == 0)

    def test_t6_divisibility(self) -> None:
        for a in range(20):
            row = {a * k for k in range(100)}
            for b in range(100):
                expected = (b == 0) if a == 0 else (b % a == 0)
                self.assertEqual(b in row, expected)

    def test_t7_sum_of_rows(self) -> None:
        for a, n in product(range(30), repeat=2):
            self.assertEqual(sum(a * j for j in range(n + 1)), a * n * (n + 1) // 2)

    def test_t8_sum_of_table(self) -> None:
        for m, n in product(range(15), repeat=2):
            self.assertEqual(sum(map(sum, table(m, n))),
                             (m * (m + 1) // 2) * (n * (n + 1) // 2))

    def test_t9_minimal_period(self) -> None:
        for a, q in product(range(50), range(2, 50)):
            p = period(a, q)
            self.assertEqual((a * p) % q, 0)
            self.assertTrue(all((a * k) % q != 0 for k in range(1, p)))

    def test_t10_distinct_residues(self) -> None:
        for a, q in product(range(50), range(2, 50)):
            self.assertEqual(len({(a * j) % q for j in range(q)}), period(a, q))

    def test_t11_invertibility(self) -> None:
        for a, q in product(range(50), range(2, 50)):
            inverses = [x for x in range(q) if (a * x) % q == 1]
            self.assertEqual(len(inverses), 1 if math.gcd(a, q) == 1 else 0)

    def test_t12_minors_and_counterexamples(self) -> None:
        for i, k, j, ell in product(range(7), repeat=4):
            self.assertEqual((i * j) * (k * ell), (i * ell) * (k * j))
        self.assertTrue(all(0 * 0 == 0 * 0 for _ in range(10)))
        self.assertFalse(certify([[0, 0], [0, 0]]))
        self.assertFalse(certify([[0, 0, 0], [0, 2, 1]]))

    def test_t13_certificate_count(self) -> None:
        for m, n in product(range(20), repeat=2):
            self.assertEqual((m + 1) + (m + 1) * n, (m + 1) * (n + 1))

    def test_t14_sum_is_insufficient(self) -> None:
        original = table(1, 2)
        wrong = [[0, 0, 0], [0, 2, 1]]
        self.assertEqual(sum(map(sum, original)), sum(map(sum, wrong)))
        self.assertFalse(certify(wrong))

    def test_exercises(self) -> None:
        self.assertEqual(7 * 11, 77)
        self.assertNotEqual(2**2, 1**2 + 1**2)
        self.assertEqual([8 * j for j in range(6)], [0, 8, 16, 24, 32, 40])
        self.assertFalse(certify([[0, 0, 0, 0, 0], [0, 7, 14, 22, 28]]))
        self.assertEqual(sum(7 * j for j in range(21)), 1470)
        self.assertEqual(sum(map(sum, table(4, 3))), 60)
        self.assertEqual([8 * j % 12 for j in range(3)], [0, 8, 4])
        self.assertEqual(5 * 5 % 12, 1)
        self.assertEqual([3 * j % 7 for j in range(7)], [0, 3, 6, 2, 5, 1, 4])
        self.assertEqual(6 * 20, 10 * 12)
        self.assertFalse(certify([[i * j + 1 for j in range(4)] for i in range(4)]))


if __name__ == "__main__":
    unittest.main()
