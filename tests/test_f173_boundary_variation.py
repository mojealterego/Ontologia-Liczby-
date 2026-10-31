"""Finite-model regression checks for F17.3 T49--T58.

Tests verify instances, not the general mathematical proofs.
"""
from __future__ import annotations

import itertools
import random
import unittest


def boundary(a: set[int]) -> set[int]:
    if not a:
        return set()
    return {n for n in range(min(a) - 1, max(a) + 1)
            if (n in a) != (n + 1 in a)}


def components(a: set[int]) -> int:
    return sum(n - 1 not in a for n in a)


def tv(f: dict[int, int]) -> int:
    support = {n for n, v in f.items() if v != 0}
    if not support:
        return 0
    return sum(abs(f.get(n + 1, 0) - f.get(n, 0))
               for n in range(min(support) - 1, max(support) + 1))


def parts(f: dict[int, int], g: dict[int, int]) -> tuple[int, int]:
    supp = {n for d in (f, g) for n, v in d.items() if v}
    if not supp:
        return 0, 0
    left = sum(f.get(n, 0) * (g.get(n + 1, 0) - g.get(n, 0))
               for n in range(min(supp) - 2, max(supp) + 2))
    right = -sum(g.get(n + 1, 0) * (f.get(n + 1, 0) - f.get(n, 0))
                 for n in range(min(supp) - 2, max(supp) + 2))
    return left, right


class BoundaryVariationTests(unittest.TestCase):
    def test_t49_t50_all_small_sets(self):
        universe = range(-3, 4)
        for mask in range(1 << 7):
            a = {n for i, n in enumerate(universe) if mask & (1 << i)}
            self.assertEqual(len(boundary(a)), 2 * components(a), a)

    def test_t51_isoperimetric_equality(self):
        for mask in range(1, 1 << 7):
            a = {i for i in range(7) if mask & (1 << i)}
            is_interval = len(a) == max(a) - min(a) + 1
            self.assertEqual(len(boundary(a)) == 2, is_interval)

    def test_t52_indicator(self):
        for mask in range(1 << 7):
            a = {i for i in range(7) if mask & (1 << i)}
            self.assertEqual(tv({n: 1 for n in a}), len(boundary(a)))

    def test_t53_max_bound_signed(self):
        for vals in itertools.product((-1, 0, 1), repeat=5):
            f = dict(zip(range(-2, 3), vals))
            self.assertGreaterEqual(tv(f), 2 * max(map(abs, vals)))

    def test_t53_sharp(self):
        for height in (-5, -1, 1, 4):
            for a in range(-3, 2):
                for b in range(a, 4):
                    f = {n: height for n in range(a, b + 1)}
                    self.assertEqual(tv(f), 2 * abs(height))

    def test_t54_integration_by_parts(self):
        rng = random.Random(173)
        for _ in range(4000):
            f = {n: rng.randrange(-3, 4) for n in range(-3, 4)}
            g = {n: rng.randrange(-3, 4) for n in range(-3, 4)}
            self.assertEqual(*parts(f, g))

    def test_t55_triangle_and_reverse(self):
        rng = random.Random(155)
        for _ in range(4000):
            f = {n: rng.randrange(-4, 5) for n in range(-3, 4)}
            g = {n: rng.randrange(-4, 5) for n in range(-3, 4)}
            h = {n: f[n] + g[n] for n in f}
            d = {n: f[n] - g[n] for n in f}
            self.assertLessEqual(tv(h), tv(f) + tv(g))
            self.assertLessEqual(abs(tv(f) - tv(g)), tv(d))

    def test_t56_symmetric_difference(self):
        sets = [{i for i in range(6) if mask & (1 << i)}
                for mask in range(1 << 6)]
        for a in sets:
            for b in sets:
                self.assertLessEqual(abs(len(boundary(a)) - len(boundary(b))),
                                     2 * len(a ^ b))

    def test_t57_coarea_exhaustive(self):
        for vals in itertools.product(range(3), repeat=5):
            f = dict(zip(range(-2, 3), vals))
            levels = [{n for n, v in f.items() if v >= k}
                      for k in range(1, max(vals, default=0) + 1)]
            self.assertEqual(tv(f), sum(len(boundary(a)) for a in levels))
            self.assertEqual(tv(f), 2 * sum(components(a) for a in levels))

    def test_t58_equality_criterion(self):
        for vals in itertools.product(range(3), repeat=5):
            if max(vals) == 0:
                continue
            f = dict(zip(range(5), vals))
            levels = [{n for n, v in f.items() if v >= k}
                      for k in range(1, max(vals) + 1)]
            all_intervals = all(components(a) == 1 for a in levels)
            self.assertEqual(tv(f) == 2 * max(vals), all_intervals)

    def test_z53_z62_examples(self):
        self.assertEqual(components({-3, -2, 1, 4, 5, 6}), 3)
        self.assertEqual(boundary(set(range(-2, 4))), {-3, 3})
        self.assertEqual(boundary({0, 2}), {-1, 0, 1, 2})
        self.assertEqual(tv({n: 2 for n in range(1, 4)}), 4)
        self.assertEqual(tv({-1: 1, 0: -1}), 4)
        f = {0: 1, 1: 3, 2: 2}
        self.assertEqual(tv(f), 6)
        self.assertEqual(tv({0: 2, 2: 2}), 8)
        self.assertEqual(abs(len(boundary({0})) - len(boundary({0, 2}))), 2)
        self.assertEqual(parts({0: 1}, {1: 1}), (1, 1))


if __name__ == '__main__':
    unittest.main()
