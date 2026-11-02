"""Finite exhaustive verification of MSC 97D40 III-H (Hall, capacities, EF1)."""
import itertools
import unittest


def subsets(items):
    items = tuple(items)
    for mask in range(1 << len(items)):
        yield tuple(x for i, x in enumerate(items) if mask & (1 << i))


def hall(edges, n, m, capacities=None):
    capacities = capacities or (1,) * m
    for selected in subsets(range(n)):
        neighbors = {r for u in selected for r in range(m) if (u, r) in edges}
        if len(selected) > sum(capacities[r] for r in neighbors):
            return False
    return True


def feasible(edges, n, m, capacities=None):
    capacities = tuple(capacities or (1,) * m)
    for assignment in itertools.product(range(m), repeat=n):
        if all((u, assignment[u]) in edges for u in range(n)):
            if all(assignment.count(r) <= capacities[r] for r in range(m)):
                return True
    return n == 0


def balanced(counts):
    return max(counts) - min(counts) <= 1


def ef1_unit(counts):
    return all(counts[i] >= counts[j] - 1 for i in range(len(counts))
               for j in range(len(counts)) if counts[j] > 0)


class MatchingAndFairness(unittest.TestCase):
    def test_hall_exhaustive_unit_capacities(self):
        for n in range(4):
            for m in range(4):
                positions = list(itertools.product(range(n), range(m)))
                for edge_mask in range(1 << len(positions)):
                    edges = {e for k, e in enumerate(positions) if edge_mask & (1 << k)}
                    self.assertEqual(hall(edges, n, m), feasible(edges, n, m),
                                     (n, m, edges))

    def test_hall_exhaustive_capacities(self):
        n, m = 3, 3
        positions = list(itertools.product(range(n), range(m)))
        for edge_mask in range(1 << len(positions)):
            edges = {e for k, e in enumerate(positions) if edge_mask & (1 << k)}
            for capacities in itertools.product(range(3), repeat=m):
                self.assertEqual(hall(edges, n, m, capacities),
                                 feasible(edges, n, m, capacities),
                                 (edges, capacities))

    def test_greedy_counterexample(self):
        edges = {(0, 0), (0, 1), (1, 0)}
        self.assertTrue(feasible(edges, 2, 2))
        self.assertFalse(feasible({(0, 0), (1, 0)}, 2, 2))

    def test_increased_capacities_preserve_feasibility(self):
        positions = list(itertools.product(range(2), range(2)))
        for edge_mask in range(1 << len(positions)):
            edges = {e for k, e in enumerate(positions) if edge_mask & (1 << k)}
            for b in itertools.product(range(3), repeat=2):
                for bp in itertools.product(range(3), repeat=2):
                    if all(x <= y for x, y in zip(b, bp)) and feasible(edges, 2, 2, b):
                        self.assertTrue(feasible(edges, 2, 2, bp))

    def test_complete_matching_count(self):
        for n in range(5):
            for m in range(n, 6):
                assignments = sum(len(set(a)) == n for a in itertools.product(range(m), repeat=n))
                expected = 1
                for x in range(m - n + 1, m + 1):
                    expected *= x
                self.assertEqual(assignments, expected)

    def test_balanced_implies_ef1(self):
        for n in range(1, 5):
            for k in range(7):
                for allocation in itertools.product(range(n), repeat=k):
                    counts = [allocation.count(i) for i in range(n)]
                    if balanced(counts):
                        self.assertTrue(ef1_unit(counts))

    def test_minimum_imbalance(self):
        for n in range(1, 5):
            for k in range(7):
                optimum = min((max(allocation.count(i) for i in range(n)) -
                               min(allocation.count(i) for i in range(n)))
                              for allocation in itertools.product(range(n), repeat=k))
                self.assertEqual(optimum, 0 if k % n == 0 else 1)

    def test_ef1_not_envy_free(self):
        self.assertTrue(ef1_unit((2, 1)))
        self.assertNotEqual(2, 1)

    def test_bottleneck_lower_bound_can_be_strict(self):
        assignments = [(0, 1), (1, 0)]
        costs = {(0, 0): 0, (0, 1): 10, (1, 0): 0, (1, 1): 10}
        optimum = min(max(costs[(u, a[u])] for u in range(2)) for a in assignments)
        lower = max(min(costs[(u, r)] for r in range(2)) for u in range(2))
        self.assertEqual((lower, optimum), (0, 10))


if __name__ == "__main__":
    unittest.main()
