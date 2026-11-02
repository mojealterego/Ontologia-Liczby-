"""Finite, independent regression tests for MSC 97D40 III-D.

No external dependencies. Run: python -m unittest -v test_msc97d40_optimization.py
"""
import itertools
import math
import unittest


def knapsack(costs, values, budget):
    if budget < 0 or len(costs) != len(values):
        raise ValueError("invalid budget or dimensions")
    if any(c <= 0 or not isinstance(c, int) for c in costs):
        raise ValueError("costs must be positive integers")
    f = [0] * (budget + 1)
    for c, v in zip(costs, values):
        for b in range(budget, c - 1, -1):
            f[b] = max(f[b], f[b-c] + v)
    return f[budget]


def brute_knapsack(costs, values, budget):
    n = len(costs)
    return max((sum(values[i] for i in range(n) if mask >> i & 1)
                for mask in range(1 << n)
                if sum(costs[i] for i in range(n) if mask >> i & 1) <= budget), default=0)


def min_cover_cost(covers, costs, universe):
    m = len(universe)
    positions = {u: i for i, u in enumerate(universe)}
    masks = [sum(1 << positions[u] for u in cover) for cover in covers]
    inf = float("inf")
    dp = [inf] * (1 << m)
    dp[0] = 0
    for mask, cost in zip(masks, costs):
        nxt = dp.copy()
        for state in range(1 << m):
            nxt[state | mask] = min(nxt[state | mask], dp[state] + cost)
        dp = nxt
    return dp[-1]


def brute_cover_cost(covers, costs, universe):
    n = len(covers)
    target = set(universe)
    return min((sum(costs[i] for i in range(n) if mask >> i & 1)
                for mask in range(1 << n)
                if set().union(*(covers[i] for i in range(n) if mask >> i & 1)) == target), default=float("inf"))


class TestOptimization(unittest.TestCase):
    def test_knapsack_example(self):
        self.assertEqual(knapsack([6, 5, 5], [9, 8, 8], 10), 16)

    def test_knapsack_exhaustive(self):
        for costs in itertools.product(range(1, 5), repeat=3):
            for values in itertools.product(range(4), repeat=3):
                for budget in range(9):
                    self.assertEqual(knapsack(costs, values, budget),
                                     brute_knapsack(costs, values, budget))

    def test_budget_monotone(self):
        results = [knapsack([3, 4, 6], [5, 7, 9], b) for b in range(15)]
        self.assertEqual(results, sorted(results))

    def test_cover_exhaustive(self):
        universe = (0, 1, 2)
        all_sets = [set(u for u in universe if mask >> u & 1) for mask in range(8)]
        for covers in itertools.product(all_sets, repeat=3):
            for costs in ((1, 1, 1), (1, 2, 3), (3, 1, 2)):
                self.assertEqual(min_cover_cost(covers, costs, universe),
                                 brute_cover_cost(covers, costs, universe))

    def test_fractional_upper_bound(self):
        for costs in itertools.product((1, 2, 3), repeat=3):
            for values in itertools.product((0, 1, 3), repeat=3):
                for budget in range(1, 7):
                    items = [(c, v) for c, v in zip(costs, values) if c <= budget]
                    ordered = sorted(items, key=lambda cv: cv[1] / cv[0], reverse=True)
                    remaining, relaxed = budget, 0.0
                    for c, v in ordered:
                        share = min(1.0, remaining / c)
                        relaxed += share * v
                        remaining -= share * c
                    optimum = brute_knapsack([c for c, _ in items], [v for _, v in items], budget)
                    self.assertGreaterEqual(relaxed + 1e-10, optimum)
                    self.assertLessEqual(relaxed, 2 * optimum + 1e-10)

    def test_random_cover_formula(self):
        for p, q in itertools.product((0.0, .25, .5, .75, 1.0), repeat=2):
            expected = 1 - (1 - p) * (1 - q)
            enumerated = p*q + p*(1-q) + (1-p)*q
            self.assertAlmostEqual(expected, enumerated)
            self.assertLessEqual((1-p)*(1-q), math.exp(-(p+q)) + 1e-12)

    def test_lower_bound_on_cover_size(self):
        self.assertEqual(math.ceil(3/2), 2)
        self.assertEqual(min_cover_cost([{0, 1}, {1, 2}], [2, 2], (0, 1, 2)), 4)

    def test_invalid_cost(self):
        with self.assertRaises(ValueError):
            knapsack([0], [3], 10)


if __name__ == "__main__":
    unittest.main()
