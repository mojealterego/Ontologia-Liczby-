"""F26.1: exhaustive finite-model checks; not a proof of infinite claims."""
from __future__ import annotations

import itertools
import math
import unittest
from collections import Counter
from fractions import Fraction


def all_maps(a_size: int, b_size: int):
    if b_size == 0 and a_size != 0:
        return
    for values in itertools.product(range(b_size), repeat=a_size):
        yield values


def image(values, subset):
    return {values[i] for i in subset}


def preimage(values, subset):
    return {i for i, v in enumerate(values) if v in subset}


def sat(values, subset):
    return preimage(values, image(values, subset))


def fibers(values, b_size):
    return {b: preimage(values, {b}) for b in range(b_size)}


def powerset(n):
    return [set(i for i in range(n) if mask & (1 << i)) for mask in range(1 << n)]


class FiberProperties(unittest.TestCase):
    def test_empty_map(self):
        self.assertEqual(list(all_maps(0, 0)), [()])
        self.assertEqual(fibers((), 0), {})
        self.assertEqual(sat((), set()), set())

    def test_no_map_to_empty_from_nonempty(self):
        self.assertEqual(list(all_maps(1, 0)), [])

    def test_t1_closure_extensive_monotone_idempotent(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    ps = powerset(n)
                    for s in ps:
                        self.assertLessEqual(s, sat(f, s))
                        self.assertEqual(sat(f, sat(f, s)), sat(f, s))
                        for t in ps:
                            if s <= t:
                                self.assertLessEqual(sat(f, s), sat(f, t))

    def test_t2_image_preimage(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    for u in powerset(m):
                        self.assertEqual(image(f, preimage(f, u)), u & set(f))

    def test_t3_saturation_as_union_of_fibers(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    for s in powerset(n):
                        union = set().union(*(preimage(f, {b}) for b in image(f, s))) if s else set()
                        self.assertEqual(sat(f, s), union)
                        self.assertEqual(s == sat(f, s), s == preimage(f, image(f, s)))

    def test_t4_intersection_iff_injective(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    p = powerset(n)
                    preserves = all(image(f, s & t) == image(f, s) & image(f, t)
                                    for s in p for t in p)
                    self.assertEqual(preserves, len(set(f)) == n)

    def test_t5_quotient_fiber_classes(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    classes = {frozenset(preimage(f, {b})) for b in set(f)}
                    self.assertEqual(len(classes), len(set(f)))
                    self.assertEqual(set().union(*map(set, classes)) if classes else set(), set(range(n)))
                    for a in range(n):
                        self.assertIn(a, preimage(f, {f[a]}))

    def test_t6_adjunction(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    for s in powerset(n):
                        for u in powerset(m):
                            self.assertEqual(image(f, s) <= u, s <= preimage(f, u))

    def test_t7_partition_count(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    self.assertEqual(sum(map(len, fibers(f, m).values())), n)

    def test_t8_inj_surj_bij(self):
        for n in range(5):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    sizes = [len(x) for x in fibers(f, m).values()]
                    self.assertEqual(max(sizes) <= 1, len(set(f)) == n)
                    self.assertEqual(min(sizes) >= 1, len(set(f)) == m)
                    self.assertEqual(all(x == 1 for x in sizes), n == m == len(set(f)))

    def test_t9_composition_fibers(self):
        for n in range(4):
            for m in range(1, 4):
                for k in range(1, 4):
                    for f in all_maps(n, m):
                        for g in all_maps(m, k):
                            composed = tuple(g[b] for b in f)
                            for c in range(k):
                                lhs = preimage(composed, {c})
                                rhs = set().union(*(preimage(f, {b}) for b in range(m) if g[b] == c))
                                self.assertEqual(lhs, rhs)

    def test_t10_cardinality_bound(self):
        for n in range(1, 6):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    M = max(Counter(f).values())
                    self.assertGreaterEqual(len(set(f)), math.ceil(n / M))

    def test_t11_factorization(self):
        # Every surjection f and every h:A->{0,1} on small finite sets.
        for n in range(1, 5):
            for m in range(1, min(n, 3) + 1):
                for f in all_maps(n, m):
                    if len(set(f)) != m:
                        continue
                    for h in all_maps(n, 2):
                        compatible = all(f[i] != f[j] or h[i] == h[j]
                                         for i in range(n) for j in range(n))
                        candidates = [k for k in all_maps(m, 2)
                                      if all(h[i] == k[f[i]] for i in range(n))]
                        self.assertEqual(len(candidates), 1 if compatible else 0)

    def test_t12_collision_probability(self):
        for n in range(2, 6):
            for m in range(1, 4):
                for f in all_maps(n, m):
                    hits = sum(f[i] == f[j] for i in range(n) for j in range(n) if i != j)
                    expected = sum(v * (v - 1) for v in Counter(f).values())
                    self.assertEqual(hits, expected)
                    self.assertEqual(Fraction(hits, n * (n - 1)),
                                     Fraction(expected, n * (n - 1)))

    def test_z1_fibers(self):
        self.assertEqual(fibers(tuple(x % 3 for x in range(5)), 3),
                         {0: {0, 3}, 1: {1, 4}, 2: {2}})

    def test_z2_saturation(self):
        self.assertEqual(sat(tuple(x % 3 for x in range(5)), {0, 2}), {0, 2, 3})

    def test_z5_image_preimage(self):
        f = {n: n * n for n in range(-10, 11)}
        self.assertEqual({f[x] for x in f if f[x] in {-1, 0, 4}}, {0, 4})

    def test_z6_probability(self):
        self.assertEqual(Fraction(3 * 2 + 2 * 1, 6 * 5), Fraction(4, 15))

    def test_z7_sharp_bound(self):
        self.assertEqual(math.ceil(Fraction(17, 4)), 5)
        self.assertEqual(sum((4, 4, 4, 4, 1)), 17)

    def test_z8_non_factorization(self):
        self.assertEqual(0 % 3, 3 % 3)
        self.assertNotEqual((-1) ** 0, (-1) ** 3)

    def test_z9_factorization(self):
        self.assertTrue(all((n % 3) == ({0: 0, 1: 1, 2: 2}[n % 3]) for n in range(-100, 101)))

    def test_z10_composition(self):
        f = tuple(x % 2 for x in range(4))
        g = (0, 0)
        self.assertEqual(preimage(tuple(g[b] for b in f), {0}), set(range(4)))

    def test_z11_union(self):
        for f in all_maps(4, 3):
            for s in powerset(4):
                for t in powerset(4):
                    self.assertEqual(sat(f, s | t), sat(f, s) | sat(f, t))

    def test_z12_injective_images(self):
        for f in all_maps(3, 4):
            if len(set(f)) != 3:
                continue
            for s in powerset(3):
                for t in powerset(3):
                    if image(f, s) == image(f, t):
                        self.assertEqual(s, t)

    def test_counterexamples(self):
        f = (0, 0)
        self.assertNotEqual(image(f, {0} & {1}), image(f, {0}) & image(f, {1}))
        self.assertNotEqual(sat(f, {0}), {0})
        self.assertNotEqual(image((0,), preimage((0,), {1})), {1})
        self.assertEqual(len(set(f)), 1)


if __name__ == '__main__':
    unittest.main()
