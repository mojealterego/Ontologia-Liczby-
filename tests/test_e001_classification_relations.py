"""E0-01: checks finite models; these do not prove general theorems."""
from __future__ import annotations

import itertools
import unittest


def classes(labels: tuple) -> list[frozenset[int]]:
    return sorted(
        (frozenset(i for i, value in enumerate(labels) if value == key)
         for key in set(labels)),
        key=lambda group: (min(group), len(group)),
    )


def equivalence_pairs(labels: tuple) -> set[tuple[int, int]]:
    return {
        (i, j)
        for i in range(len(labels))
        for j in range(len(labels))
        if labels[i] == labels[j]
    }


def is_equivalence(rel: set[tuple[int, int]], n: int) -> bool:
    return (
        all((x, x) in rel for x in range(n))
        and all((y, x) in rel for x, y in rel)
        and all(
            (x, z) in rel
            for x in range(n)
            for y in range(n)
            for z in range(n)
            if (x, y) in rel and (y, z) in rel
        )
    )


def is_partial_order(rel: set[tuple[int, int]], n: int) -> bool:
    return (
        all((x, x) in rel for x in range(n))
        and all(x == y for x, y in rel if (y, x) in rel)
        and all(
            (x, z) in rel
            for x in range(n)
            for y in range(n)
            for z in range(n)
            if (x, y) in rel and (y, z) in rel
        )
    )


class TestE001(unittest.TestCase):
    def test_partitions_exhaustive(self):
        for n in range(7):
            for labels in itertools.product(range(3), repeat=n):
                groups = classes(labels)
                union = set().union(*groups) if groups else set()
                self.assertEqual(union, set(range(n)))
                self.assertEqual(sum(map(len, groups)), n)
                self.assertTrue(all(not a & b
                                    for i, a in enumerate(groups)
                                    for b in groups[i + 1:]))

    def test_equivalence_exhaustive(self):
        for n in range(6):
            for labels in itertools.product(range(3), repeat=n):
                self.assertTrue(is_equivalence(equivalence_pairs(labels), n))

    def test_refinement_exhaustive(self):
        for n in range(5):
            labelings = list(itertools.product(range(3), repeat=n))
            for coarse in labelings:
                for fine in labelings:
                    if all(fine[i] != fine[j] or coarse[i] == coarse[j]
                           for i in range(n) for j in range(n)):
                        for group in classes(fine):
                            self.assertTrue(any(group <= candidate
                                                for candidate in classes(coarse)))

    def test_similarity_is_not_transitive(self):
        rel = {(x, y) for x in (1, 2, 3) for y in (1, 2, 3)
               if abs(x - y) <= 1}
        self.assertIn((1, 2), rel)
        self.assertIn((2, 3), rel)
        self.assertNotIn((1, 3), rel)

    def test_subset_is_partial_not_total(self):
        family = (frozenset({1}), frozenset({2}), frozenset({1, 2}))
        rel = {(i, j) for i, a in enumerate(family)
               for j, b in enumerate(family) if a <= b}
        self.assertTrue(is_partial_order(rel, len(family)))
        self.assertNotIn((0, 1), rel)
        self.assertNotIn((1, 0), rel)

    def test_finite_partial_orders_have_minimal_element(self):
        for n in range(1, 4):
            edges = [(i, j) for i in range(n)
                     for j in range(n) if i != j]
            for choices in itertools.product((0, 1), repeat=len(edges)):
                rel = {(i, i) for i in range(n)}
                rel |= {edge for edge, flag in zip(edges, choices) if flag}
                if is_partial_order(rel, n):
                    self.assertTrue(any(
                        not any((j, i) in rel and j != i for j in range(n))
                        for i in range(n)
                    ))

    def test_periodic_blocks(self):
        for block in (("K", "K", "T"), ("R", "G", "B"), (0, 1)):
            for k in range(100):
                self.assertEqual(
                    (block * (k // len(block) + 1))[k],
                    block[k % len(block)],
                )
        self.assertEqual(("K", "K", "T")[20 % 3], "T")

    def test_inclusion_exclusion_exercise(self):
        objects = [("red", "circle"), ("red", "circle"),
                   ("red", "heart"), ("green", "circle"),
                   ("green", "triangle")]
        red = {i for i, (c, _) in enumerate(objects) if c == "red"}
        circles = {i for i, (_, s) in enumerate(objects) if s == "circle"}
        self.assertEqual((len(red), len(circles), len(red & circles)),
                         (3, 3, 2))
        self.assertEqual(len(red | circles), 4)

    def test_equivalence_pair_count(self):
        self.assertEqual(len(equivalence_pairs((0, 0, 1, 0))), 10)
        self.assertEqual(len(classes((0, 0, 1, 0))), 2)

    def test_two_feature_partition(self):
        labels = (("hard", True), ("hard", False),
                  ("hard", False), ("soft", True), ("soft", False))
        self.assertEqual(sorted(map(len, classes(labels))),
                         [1, 1, 1, 2])

    def test_two_extensions_of_finite_sequence(self):
        for prefix in itertools.product(("A", "B"), repeat=4):
            a = prefix + ("A",) * 4
            b = prefix + ("B",) * 4
            self.assertEqual(a[:4], b[:4])
            self.assertNotEqual(a, b)

    def test_relabeling_preserves_class_sizes(self):
        labels = (0, 1, 0, 2, 1, 0)
        expected = sorted(map(len, classes(labels)))
        for perm in itertools.permutations(range(len(labels))):
            actual = tuple(labels[i] for i in perm)
            self.assertEqual(sorted(map(len, classes(actual))),
                             expected)


if __name__ == "__main__":
    unittest.main()
