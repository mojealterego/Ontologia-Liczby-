"""Finite checks for F17.3 T27–T37. Not a substitute for proofs."""
from __future__ import annotations

import itertools
import unittest


def nearest_lattice(x: int, a: int, h: int) -> tuple[int, ...]:
    if h < 1:
        raise ValueError("h must be positive")
    q, r = divmod(x - a, h)
    candidates = (a + q * h, a + (q + 1) * h)
    d = min(abs(x - z) for z in candidates)
    return tuple(z for z in candidates if abs(x - z) == d)


class OrderConvexityTests(unittest.TestCase):
    def test_t27_convex_subsets(self) -> None:
        domain = tuple(range(-3, 4))
        for mask in range(1 << len(domain)):
            a = {x for i, x in enumerate(domain) if mask & (1 << i)}
            definition = all(not (x <= z <= y) or z in a
                             for x, y, z in itertools.product(a, a, domain))
            classification = not a or len(a) == max(a) - min(a) + 1
            self.assertEqual(definition, classification)

    def test_t28_hull(self) -> None:
        for a in itertools.combinations(range(-5, 6), 3):
            self.assertEqual(len(set(range(min(a), max(a) + 1))), max(a) - min(a) + 1)

    def test_t29_helly_t30_intersection(self) -> None:
        intervals = [(a, b) for a in range(-3, 4) for b in range(a, 4)]
        for group in itertools.combinations(intervals, 3):
            sets = [set(range(a, b + 1)) for a, b in group]
            intersection = set.intersection(*sets)
            formula = max(0, min(b for _, b in group) - max(a for a, _ in group) + 1)
            self.assertEqual(len(intersection), formula)
            if all(sets[i] & sets[j] for i in range(3) for j in range(i + 1, 3)):
                self.assertTrue(intersection)

    def test_t31_nearest_lattice(self) -> None:
        for h, a, x in itertools.product(range(1, 12), range(-3, 4), range(-25, 26)):
            result = nearest_lattice(x, a, h)
            candidates = [a + h * k for k in range(-35, 36)]
            best = min(abs(x - z) for z in candidates)
            self.assertEqual(result, tuple(z for z in candidates if abs(x - z) == best))

    def test_t32_count_lattice(self) -> None:
        for h, a, u in itertools.product(range(1, 10), range(-3, 4), range(-6, 7)):
            for v in range(u, 7):
                lo = -((a - u) // h)
                hi = (v - a) // h
                expected = max(0, hi - lo + 1)
                actual = sum((n - a) % h == 0 for n in range(u, v + 1))
                self.assertEqual(expected, actual)

    def test_t33_periodicity_symmetry(self) -> None:
        for h, a, x in itertools.product(range(1, 11), range(-3, 4), range(-12, 13)):
            d = min(abs(x - z) for z in nearest_lattice(x, a, h))
            periodic = min(abs(x + h - z) for z in nearest_lattice(x + h, a, h))
            reflected = min(abs(2 * a - x - z) for z in nearest_lattice(2 * a - x, a, h))
            self.assertEqual(d, periodic)
            self.assertEqual(d, reflected)
            self.assertLessEqual(d, h // 2)

    def test_t34_telescope(self) -> None:
        f = lambda n: n * n - 3 * n + 7
        for a in range(-8, 8):
            for b in range(a + 1, 9):
                self.assertEqual(f(b) - f(a), sum(f(n + 1) - f(n) for n in range(a, b)))

    def test_t35_monotonicity(self) -> None:
        f = lambda n: 5 * n - 7
        for a in range(-15, 15):
            self.assertGreater(f(a + 1), f(a))

    def test_t36_second_differences(self) -> None:
        for c, d, n in itertools.product(range(0, 5), range(-5, 6), range(-15, 16)):
            f = lambda t: c * t * t + d * t + 3
            self.assertEqual(f(n + 2) - 2 * f(n + 1) + f(n), 2 * c)

    def test_t37_local_global_minimum(self) -> None:
        for center in range(-5, 6):
            f = lambda n: (n - center) ** 2
            for t in range(-9, 10):
                local = f(t) <= f(t - 1) and f(t) <= f(t + 1)
                global_min = f(t) == min(f(n) for n in range(-30, 31))
                self.assertEqual(local, global_min)

    def test_solved_examples(self) -> None:
        self.assertEqual(nearest_lattice(5, 1, 8), (1, 9))
        self.assertEqual(nearest_lattice(-4, 2, 5), (-3,))
        self.assertEqual(min(abs(23 - z) for z in nearest_lattice(23, 1, 6)), 2)
        self.assertEqual(min(abs(-23 - z) for z in nearest_lattice(-23, 1, 6)), 0)


if __name__ == "__main__":
    unittest.main()
