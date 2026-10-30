"""Reprodukowalne kontrole przykładów F9.3 i F9.4.

Nie są dowodem wszystkich twierdzeń ani recenzją naukową manuskryptu.
Uruchomienie z katalogu repozytorium: python -m unittest discover -s tests -p test_f93_f94.py -v
"""
from __future__ import annotations

import itertools
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "manuscript" / "tom-01" / "F09"


class TestF93F94(unittest.TestCase):
    def test_f93_finite_agreement_not_identity(self) -> None:
        for bound in (0, 1, 2, 7, 15):
            q = lambda x: math.prod(x - k for k in range(bound + 1))
            self.assertTrue(all(q(k) == 0 for k in range(bound + 1)))
            self.assertEqual(q(bound + 1), math.factorial(bound + 1))

    def test_f93_prime_polynomial_counterexample(self) -> None:
        self.assertEqual(40 * 40 + 40 + 41, 41 * 41)

    def test_f93_inclusion_exclusion(self) -> None:
        a, b = set(range(19)), set(range(12, 25))
        self.assertEqual((len(a), len(b), len(a & b), len(a | b)), (19, 13, 7, 25))

    def test_f93_stream_distinct_counts(self) -> None:
        seq = (2, 5, 2, 7, 5, 9)
        self.assertEqual([len(set(seq[:k])) for k in range(len(seq) + 1)], [0, 1, 2, 2, 3, 3, 4])

    def test_f94_permutations_with_exactly_one_fixed_point(self) -> None:
        perms = itertools.permutations(range(4))
        self.assertEqual(sum(sum(x == i for i, x in enumerate(p)) == 1 for p in perms), 8)

    def test_f94_surjections(self) -> None:
        count = sum(len(set(f)) == 3 for f in itertools.product(range(3), repeat=4))
        self.assertEqual(count, 36)

    def test_f94_symmetric_reflexive_relations(self) -> None:
        universe = range(4)
        pairs = list(itertools.combinations(universe, 2))
        all_relations = set()
        for mask in range(1 << len(pairs)):
            relation = {(i, i) for i in universe}
            for bit, (a, b) in enumerate(pairs):
                if (mask >> bit) & 1:
                    relation.update({(a, b), (b, a)})
            all_relations.add(frozenset(relation))
        self.assertEqual(len(all_relations), 64)

    def test_f94_monotone_paths(self) -> None:
        paths = []
        for ups in itertools.combinations(range(7), 3):
            x = y = 0
            trajectory = [(x, y)]
            for step in range(7):
                if step in ups:
                    y += 1
                else:
                    x += 1
                trajectory.append((x, y))
            self.assertEqual((x, y), (4, 3))
            paths.append(trajectory)
        self.assertEqual(len(paths), 35)
        self.assertEqual(sum((2, 1) in p for p in paths), 18)

    def test_f94_stars_and_bars(self) -> None:
        sols = [(x, y, 10-x-y) for x in range(11) for y in range(11-x)]
        self.assertEqual(len(sols), 66)
        self.assertEqual(sum(min(z) >= 1 for z in sols), 36)

    def test_f94_three_sets_inclusion_exclusion(self) -> None:
        portions = [8, 5, 5, 3, 2, 4, 2]
        self.assertEqual(sum(portions), 29)
        A = set(range(0,8)) | set(range(18,21)) | set(range(21,23)) | set(range(27,29))
        B = set(range(8,13)) | set(range(18,21)) | set(range(23,27)) | set(range(27,29))
        C = set(range(13,18)) | set(range(21,23)) | set(range(23,27)) | set(range(27,29))
        self.assertEqual((len(A), len(B), len(C), len(A&B), len(A&C), len(B&C), len(A&B&C), len(A|B|C)),(15,14,13,5,4,6,2,29))

    def test_f94_pigeonhole_sharp_bound(self) -> None:
        distribution = (13, 13, 13, 13, 13, 12, 12, 12)
        self.assertEqual(sum(distribution), 101)
        self.assertEqual(max(distribution), 13)
        self.assertLess(8 * 12, 101)

    def test_f94_parity_invariant_under_two_flips(self) -> None:
        n = 6
        initial = sum(1 << i for i in range(3))
        reachable = {initial}
        for _ in range(5):
            reachable |= {state ^ (1 << a) ^ (1 << b)
                          for state in reachable
                          for a, b in itertools.combinations(range(n), 2)}
        self.assertTrue(all(state.bit_count() % 2 == 1 for state in reachable))

    def test_f94_handshake(self) -> None:
        n = 12
        E = list(itertools.combinations(range(n), 2))[:19]
        deg = [0] * n
        for a, b in E:
            deg[a] += 1
            deg[b] += 1
        self.assertEqual(sum(deg), 38)
        self.assertEqual(sum(d % 2 for d in deg) % 2, 0)

    def test_f94_chinese_remainder(self) -> None:
        sols = [x for x in range(100) if x % 5 == 2 and x % 7 == 3]
        self.assertEqual(sols, [17, 52, 87])
        self.assertTrue(all((17 + 35*t)%5 == 2 and (17 + 35*t)%7 == 3 for t in range(-10,11)))

    def test_f94_marked_subsets(self) -> None:
        for n in range(1, 18):
            self.assertEqual(sum(k * math.comb(n, k) for k in range(n+1)), n * 2**(n-1))

    def test_f94_pascals_identity(self) -> None:
        for n in range(1, 19):
            for k in range(n+1):
                c = (lambda x,y: math.comb(x,y) if 0<=y<=x else 0)
                self.assertEqual(math.comb(n,k), c(n-1,k)+c(n-1,k-1))
        self.assertEqual(math.comb(10, 4), 210)

    def test_manuscript_has_exactly_twelve_distinct_tasks_per_point(self) -> None:
        for name in ("F9.3_UZUPELNIENIE_ODLICZANIE_A_DOWOD.md", "F9.4_UZUPELNIENIE_ZADANIA_Z_DOWODAMI.md"):
            content = (ROOT / name).read_text(encoding="utf-8")
            matches = [int(x) for x in re.findall(r"\*\*Zadanie\s+(\d+)\b", content)] if "F9.3" in name else [int(x) for x in re.findall(r"^### Zadanie\s+(\d+)\b", content, re.MULTILINE)]
            self.assertEqual(matches, list(range(1, 13)), msg=name)
            self.assertGreater(len(content), 12000)
            self.assertNotIn("TODO", content)


if __name__ == "__main__":
    unittest.main()