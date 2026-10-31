"""Finite property checks for F17.3 T38--T48 (not formal proofs)."""
from __future__ import annotations

import itertools
import math
import unittest


def centers(points, lo=-25, hi=25):
    energies = {t: max(abs(t - s) for s in points) for t in range(lo, hi + 1)}
    best = min(energies.values())
    return best, {t for t, v in energies.items() if v == best}


def nearest_to_set(t, points):
    return min(abs(t - s) for s in points)


def weighted_median_set(points, weights, lo=-20, hi=20):
    vals = {t: sum(w * abs(t - a) for a, w in zip(points, weights)) for t in range(lo, hi + 1)}
    best = min(vals.values())
    return {t for t, val in vals.items() if val == best}


def weighted_median_criterion(points, weights, lo=-20, hi=20):
    W = sum(weights)
    return {t for t in range(lo, hi + 1)
            if 2 * sum(w for a, w in zip(points, weights) if a <= t - 1) <= W
            and W <= 2 * sum(w for a, w in zip(points, weights) if a <= t)}


class F173CentersConvexPaths(unittest.TestCase):
    def test_centers_exhaustive(self):
        universe = range(-4, 5)
        for size in range(1, 5):
            for points in itertools.combinations(universe, size):
                r, C = centers(points)
                m, M = min(points), max(points)
                self.assertEqual(r, (M - m + 1) // 2)
                self.assertEqual(C, {math.floor((m + M) / 2), math.ceil((m + M) / 2)})

    def test_centers_in_restricted_interval(self):
        for S in [(-9, -2, 4, 12), (-2, 7), (0,), (-8, 1, 5)]:
            for u in range(-7, 5):
                for v in range(u, 8):
                    energies = {t: max(abs(t - s) for s in S) for t in range(u, v + 1)}
                    q = (min(S) + max(S)) / 2
                    best = min(energies.values())
                    argmin = {t for t, value in energies.items() if value == best}
                    d = min(abs(t - q) for t in range(u, v + 1))
                    self.assertEqual(argmin, {t for t in range(u, v + 1) if abs(t - q) == d})

    def test_center_radius_stability(self):
        for a in range(-4, 3):
            for b in range(a, 5):
                for c in range(-4, 3):
                    for d in range(c, 5):
                        h = max(abs(a - c), abs(b - d))
                        self.assertLessEqual(abs(centers((a, b))[0] - centers((c, d))[0]), h)

    def test_weighted_median_exhaustive(self):
        for points in itertools.product(range(-2, 3), repeat=3):
            for weights in itertools.product(range(1, 4), repeat=3):
                self.assertEqual(weighted_median_set(points, weights),
                                 weighted_median_criterion(points, weights))

    def test_distance_lipschitz(self):
        for size in range(1, 4):
            for points in itertools.combinations(range(-3, 4), size):
                for x in range(-6, 7):
                    for y in range(-6, 7):
                        self.assertLessEqual(abs(nearest_to_set(x, points) - nearest_to_set(y, points)),
                                             abs(x - y))

    def test_path_counts_by_enumeration(self):
        for k in range(0, 10):
            counts = {}
            for steps in itertools.product((-1, 1), repeat=k):
                endpoint = sum(steps)
                counts[endpoint] = counts.get(endpoint, 0) + 1
            for diff in range(-11, 12):
                expected = math.comb(k, (k + diff) // 2) if k >= abs(diff) and (k - diff) % 2 == 0 else 0
                self.assertEqual(counts.get(diff, 0), expected)

    def test_strong_convexity_two_adjacent_minima(self):
        for a in range(1, 5):
            for b in range(-9, 10):
                vals = {n: a * n * n + b * n for n in range(-20, 21)}
                v = min(vals.values())
                minimizers = [n for n, f in vals.items() if f == v]
                self.assertLessEqual(len(minimizers), 2)
                self.assertLessEqual(max(minimizers) - min(minimizers), 1)

    def test_convex_chord(self):
        for a in range(-5, 5):
            for b in range(a + 2, 7):
                for t in range(a + 1, b):
                    for c in (-3, 0, 5):
                        f = lambda n: n * n + c * n
                        self.assertLessEqual((b - a) * f(t), (b - t) * f(a) + (t - a) * f(b))

    def test_coercivity_example(self):
        f = lambda n: n * n + 3 * n
        self.assertEqual({n for n in range(-100, 101) if f(n) == -2}, {-2, -1})
        self.assertEqual(2 * (-3) + 4, -2)
        self.assertEqual(2 * (-1) + 4, 2)

    def test_examples_z39_z52(self):
        self.assertEqual(centers((-9, -2, 4, 12)), (11, {1, 2}))
        S = (-9, -2, 4, 12)
        self.assertEqual(min(range(-8, -2), key=lambda t: max(abs(t - s) for s in S)), -3)
        self.assertEqual(max(abs(-3 - s) for s in S), 15)
        self.assertEqual(weighted_median_set((-3, 2, 8), (1, 5, 2)), {2})
        self.assertEqual(weighted_median_set((0, 10), (3, 3)), set(range(11)))
        self.assertEqual({n for n in range(-10, 11) if 2*n*n - 7*n + 5 == -1}, {2})
        self.assertEqual({n for n in range(-10, 11) if n*n - n + 6 == 6}, {0, 1})
        self.assertEqual(math.comb(6, 4), 15)
        self.assertEqual(math.comb(7, 2), 21)
        self.assertEqual((nearest_to_set(4, (-7, 0, 11)), nearest_to_set(5, (-7, 0, 11))), (4, 5))
        self.assertEqual(centers((-4, 5))[0], centers((-2, 7))[0])

    def test_existing_median_claim(self):
        for n in range(1, 5):
            for values in itertools.combinations_with_replacement(range(-3, 4), n):
                scores = {t: sum(abs(t - a) for a in values) for t in range(-8, 9)}
                best = min(scores.values())
                observed = {t for t, score in scores.items() if score == best}
                expected = {values[n//2]} if n % 2 else set(range(values[n//2-1], values[n//2]+1))
                self.assertEqual(observed, expected)


if __name__ == "__main__":
    unittest.main()
