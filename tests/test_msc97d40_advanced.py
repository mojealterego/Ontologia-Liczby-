"""MSC 97D40 III-A: exhaustive checks of weighted coverage and diagnostic bounds."""
import itertools
import math
import unittest


def score(chosen, covers, weights):
    covered = set()
    for i in chosen:
        covered |= covers[i]
    return sum(weights[u] for u in covered)


def greedy(covers, weights, k):
    chosen = []
    for _ in range(k):
        candidates = [j for j in range(len(covers)) if j not in chosen]
        if not candidates:
            break
        j = max(candidates, key=lambda j: (score(chosen + [j], covers, weights) - score(chosen, covers, weights), -j))
        chosen.append(j)
    return chosen


def optimum(covers, weights, k):
    n = len(covers)
    return max(score(c, covers, weights) for t in range(k + 1) for c in itertools.combinations(range(n), t))


class TestMSC97D40Advanced(unittest.TestCase):
    def test_greedy_bound_exhaustive(self):
        universe = range(3)
        possible = [{i for i in universe if mask & (1 << i)} for mask in range(8)]
        for weights in ({0: 1, 1: 1, 2: 1}, {0: 1, 1: 2, 2: 5}):
            for covers in itertools.product(possible, repeat=3):
                for k in (1, 2, 3):
                    actual = score(greedy(covers, weights, k), covers, weights)
                    opt = optimum(covers, weights, k)
                    bound = (1 - (1 - 1/k)**k) * opt
                    self.assertGreaterEqual(actual + 1e-10, bound)
    def test_submodularity_exhaustive(self):
        covers = [{0, 1}, {1, 2}, {0, 3}, {2, 3}]
        weights = {0: 1, 1: 2, 2: 3, 3: 5}
        for ma in range(16):
            A = {i for i in range(4) if ma & (1 << i)}
            for mb in range(16):
                B = {i for i in range(4) if mb & (1 << i)}
                if A <= B:
                    for j in set(range(4)) - B:
                        left = score(A | {j}, covers, weights) - score(A, covers, weights)
                        right = score(B | {j}, covers, weights) - score(B, covers, weights)
                        self.assertGreaterEqual(left, right)
    def test_greedy_not_always_optimal(self):
        covers = [{1, 2, 3, 4}, {1, 2, 5}, {3, 4, 6}]
        weights = {i: 1 for i in range(1, 7)}
        self.assertEqual(score(greedy(covers, weights, 2), covers, weights), 5)
        self.assertEqual(optimum(covers, weights, 2), 6)
    def test_ratio_greedy_knapsack_counterexample(self):
        B, epsilon = 100, 0.1
        self.assertGreater((1 + epsilon) / 1, B / B)
        self.assertLess((1 + epsilon) / B, 0.02)
    def test_binary_information_bound(self):
        for n in range(1, 257):
            m = math.ceil(math.log2(n))
            self.assertGreaterEqual(2**m, n)
            if n > 1:
                self.assertLess(2**(m-1), n)
    def test_binary_code_injective(self):
        for n in range(1, 65):
            m = math.ceil(math.log2(n))
            codes = [format(i, '0%db' % m) if m else '' for i in range(n)]
            self.assertEqual(len(set(codes)), n)
    def test_expected_coverage_correlated(self):
        outcomes = [(0, 0), (1, 1)]
        mean = sum(2*a + 5*b for a, b in outcomes)/2
        self.assertEqual(mean, 2*.5 + 5*.5)
    def test_expected_coverage_example(self):
        self.assertEqual(2*(1/2) + 5*(4/5), 5)
    def test_greedy_bound_k2_k3(self):
        self.assertEqual(1-(1-1/2)**2, .75)
        self.assertAlmostEqual(1-(1-1/3)**3, 19/27)
    def test_coverage_examples(self):
        covers = [{'a','b'}, {'b','c'}]
        weights = {'a':2,'b':3,'c':5}
        self.assertEqual(score([0,1],covers,weights),10)
        self.assertEqual(score([0,1],covers,weights)-score([0],covers,weights),5)

if __name__ == '__main__':
    unittest.main()
