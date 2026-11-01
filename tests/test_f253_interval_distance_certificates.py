"""F25.3: exact rational certificates for finite unions of closed intervals."""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations_with_replacement
import unittest

Interval = tuple[Q, Q]


def normalize(intervals: list[Interval]) -> list[Interval]:
    if not intervals:
        return []
    ordered = sorted((Q(a), Q(b)) for a, b in intervals)
    if any(a > b for a, b in ordered):
        raise ValueError("left endpoint greater than right endpoint")
    out: list[Interval] = []
    for a, b in ordered:
        if out and a <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return out


def distance(x: Q, intervals: list[Interval]) -> Q:
    if not intervals:
        raise ValueError("nonempty compact set required")
    return min(max(a - x, Q(0), x - b) for a, b in intervals)


def projections(x: Q, intervals: list[Interval]) -> set[Q]:
    ds = distance(x, intervals)
    candidates = set()
    for a, b in normalize(intervals):
        p = min(b, max(a, x))
        if abs(p - x) == ds:
            candidates.add(p)
    return candidates


def dilate(intervals: list[Interval], r: Q) -> list[Interval]:
    if r < 0:
        raise ValueError("negative radius")
    return normalize([(a - r, b + r) for a, b in intervals])


def erode(intervals: list[Interval], r: Q) -> list[Interval]:
    if r < 0:
        raise ValueError("negative radius")
    return [(a + r, b - r) for a, b in normalize(intervals) if b - a >= 2 * r]


def radius(intervals: list[Interval], left: Q, right: Q) -> Q:
    if not intervals or left >= right:
        raise ValueError("nonempty set and strict window required")
    pieces = normalize(intervals)
    candidates = [left, right]
    for (_, b), (a, _) in zip(pieces, pieces[1:]):
        mid = (a + b) / 2
        if left <= mid <= right:
            candidates.append(mid)
    return max(distance(x, pieces) for x in candidates)


def contains_window(intervals: list[Interval], left: Q, right: Q) -> bool:
    return any(a <= left and right <= b for a, b in normalize(intervals))


def hausdorff(a: list[Interval], b: list[Interval]) -> Q:
    if not a or not b:
        raise ValueError("nonempty sets required")
    aa, bb = normalize(a), normalize(b)
    def directed(src: list[Interval], target: list[Interval]) -> Q:
        # Distance to a fixed target is piecewise linear with possible peaks
        # at the midpoints of target gaps, so include them when inside src.
        candidates = [x for lo, hi in src for x in (lo, hi)]
        for (_, hi), (lo, _) in zip(target, target[1:]):
            mid = (lo + hi) / 2
            if any(a <= mid <= b for a, b in src):
                candidates.append(mid)
        return max(distance(x, target) for x in candidates)
    return max(directed(aa, bb), directed(bb, aa))


class TestF253(unittest.TestCase):
    def test_normalization_touching(self):
        self.assertEqual(normalize([(Q(3), Q(5)), (Q(0), Q(2)), (Q(2), Q(4)), (Q(8), Q(9))]), [(Q(0), Q(5)), (Q(8), Q(9))])

    def test_normalization_idempotent(self):
        for a in range(-3, 3):
            for b in range(a, 4):
                for c in range(-3, 3):
                    for d in range(c, 4):
                        v = [(Q(a), Q(b)), (Q(c), Q(d))]
                        self.assertEqual(normalize(normalize(v)), normalize(v))

    def test_normalization_permutation(self):
        v = [(Q(-3), Q(-1)), (Q(0), Q(2)), (Q(2), Q(4))]
        self.assertEqual(normalize(v), normalize(v[::-1]))

    def test_invalid_interval(self):
        with self.assertRaises(ValueError):
            normalize([(Q(2), Q(1))])

    def test_empty_distance(self):
        with self.assertRaises(ValueError):
            distance(Q(0), [])

    def test_distance_formula(self):
        v = [(Q(0), Q(1)), (Q(3), Q(4))]
        self.assertEqual([distance(Q(x), v) for x in [-2, 0, 1, 2, 3, 5]], [2, 0, 0, 1, 0, 1])

    def test_distance_one_lipschitz_exhaustive(self):
        v = [(Q(-2), Q(-1)), (Q(1), Q(3))]
        grid = [Q(i, 3) for i in range(-18, 19)]
        for x in grid:
            for y in grid:
                self.assertLessEqual(abs(distance(x, v) - distance(y, v)), abs(x - y))

    def test_projection_tie(self):
        self.assertEqual(projections(Q(0), [(Q(-2), Q(-1)), (Q(1), Q(2))]), {Q(-1), Q(1)})

    def test_projection_unique(self):
        self.assertEqual(projections(Q(2), [(Q(0), Q(1)), (Q(4), Q(5))]), {Q(1)})

    def test_projection_inside(self):
        self.assertEqual(projections(Q(3, 2), [(Q(1), Q(2))]), {Q(3, 2)})

    def test_dilate_touch(self):
        self.assertEqual(dilate([(Q(0), Q(1)), (Q(3), Q(4))], Q(1)), [(Q(-1), Q(5))])

    def test_dilate_membership_grid(self):
        v = [(Q(0), Q(1)), (Q(3), Q(4))]
        for r in [Q(0), Q(1, 2), Q(1), Q(2)]:
            for x in [Q(i, 4) for i in range(-12, 29)]:
                self.assertEqual(distance(x, v) <= r, any(a <= x <= b for a, b in dilate(v, r)))

    def test_erode(self):
        self.assertEqual(erode([(Q(0), Q(3)), (Q(5), Q(6))], Q(1, 2)), [(Q(1, 2), Q(5, 2)), (Q(11, 2), Q(11, 2))])

    def test_erode_empty(self):
        self.assertEqual(erode([(Q(0), Q(1))], Q(3, 4)), [])

    def test_erode_touching_components(self):
        self.assertEqual(erode([(Q(0), Q(1)), (Q(1), Q(2))], Q(3, 4)), [(Q(3, 4), Q(5, 4))])

    def test_erode_grid(self):
        v = [(Q(-2), Q(-1)), (Q(1), Q(3))]
        for r in [Q(0), Q(1, 2), Q(1)]:
            for x in [Q(i, 4) for i in range(-16, 20)]:
                # An interval [x-r,x+r] fits inside a component iff both endpoints fit.
                expected = any(a <= x-r and x+r <= b for a, b in normalize(v))
                self.assertEqual(expected, any(a <= x <= b for a, b in erode(v, r)))

    def test_radius_gap(self):
        self.assertEqual(radius([(Q(0), Q(1)), (Q(3), Q(4))], Q(0), Q(4)), Q(1))

    def test_radius_outside(self):
        self.assertEqual(radius([(Q(1), Q(2))], Q(-2), Q(4)), Q(3))

    def test_radius_bruteforce_grid(self):
        v = [(Q(-2), Q(-1)), (Q(1), Q(3))]
        for left in [Q(-4), Q(-1), Q(0), Q(2)]:
            for right in [Q(3), Q(4), Q(5)]:
                if left >= right:
                    continue
                exact = radius(v, left, right)
                sampled = max(distance(left + (right-left)*Q(i, 100), v) for i in range(101))
                self.assertLessEqual(sampled, exact)
                self.assertLessEqual(exact-sampled, (right-left)/100)

    def test_cover_equivalence(self):
        v = [(Q(0), Q(1)), (Q(3), Q(4))]
        for r in [Q(0), Q(1, 2), Q(1), Q(2)]:
            self.assertEqual(radius(v, Q(0), Q(4)) <= r, contains_window(dilate(v, r), Q(0), Q(4)))

    def test_hausdorff_shift(self):
        self.assertEqual(hausdorff([(Q(0), Q(1))], [(Q(1, 10), Q(11, 10))]), Q(1, 10))

    def test_hausdorff_symmetric(self):
        a, b = [(Q(0), Q(1)), (Q(4), Q(5))], [(Q(0), Q(5))]
        self.assertEqual(hausdorff(a, b), hausdorff(b, a))
        self.assertEqual(hausdorff(a, b), Q(3, 2))

    def test_hausdorff_distance_stability(self):
        a, b = [(Q(-2), Q(-1)), (Q(1), Q(3))], [(Q(-2), Q(0)), (Q(2), Q(3))]
        h = hausdorff(a, b)
        for x in [Q(i, 3) for i in range(-20, 21)]:
            self.assertLessEqual(abs(distance(x, a)-distance(x, b)), h)

    def test_hausdorff_radius_stability(self):
        a, b = [(Q(0), Q(1)), (Q(3), Q(4))], [(Q(0), Q(3, 2)), (Q(3), Q(4))]
        self.assertLessEqual(abs(radius(a, Q(0), Q(4))-radius(b, Q(0), Q(4))), hausdorff(a, b))

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            dilate([(Q(0), Q(1))], Q(-1))
        with self.assertRaises(ValueError):
            erode([(Q(0), Q(1))], Q(-1))

    def test_invalid_window(self):
        with self.assertRaises(ValueError):
            radius([(Q(0), Q(1))], Q(2), Q(1))

    def test_empty_hausdorff(self):
        with self.assertRaises(ValueError):
            hausdorff([], [(Q(0), Q(1))])

    def test_all_twelve_examples(self):
        u = normalize([(Q(3), Q(5)), (Q(0), Q(2)), (Q(2), Q(4)), (Q(8), Q(9))])
        self.assertEqual(u, [(Q(0), Q(5)), (Q(8), Q(9))])
        self.assertEqual(distance(Q(7), u), Q(1))
        self.assertEqual(projections(Q(13, 2), u), {Q(5), Q(8)})
        self.assertEqual(dilate([(Q(0), Q(1)), (Q(3), Q(4))], Q(1)), [(Q(-1), Q(5))])
        self.assertEqual(erode([(Q(0), Q(3)), (Q(5), Q(6))], Q(1, 2)), [(Q(1, 2), Q(5, 2)), (Q(11, 2), Q(11, 2))])
        self.assertEqual(erode([(Q(0), Q(1))], Q(3, 4)), [])
        self.assertEqual(radius([(Q(0), Q(1)), (Q(3), Q(4))], Q(0), Q(4)), Q(1))
        self.assertFalse(contains_window(dilate([(Q(0), Q(1)), (Q(3), Q(4))], Q(3, 4)), Q(0), Q(4)))
        self.assertTrue(contains_window(dilate([(Q(0), Q(1)), (Q(3), Q(4))], Q(1)), Q(0), Q(4)))
        self.assertEqual(hausdorff([(Q(0), Q(2))], [(Q(1, 4), Q(9, 4))]), Q(1, 4))
        self.assertEqual([min(Q(5), max(Q(2), x)) for x in [-3, 3, 9]], [2, 3, 5])
        self.assertEqual(radius([(Q(1), Q(2))], Q(-2), Q(4)), Q(3))


if __name__ == "__main__":
    unittest.main()
