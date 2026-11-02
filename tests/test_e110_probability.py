"""E1-10: deterministic, exact-fraction tests of finite probability.

No floating-point comparison is used. Exhaustive checks cover all pairs of
events on a four-outcome space, plus textbook examples from the manuscript.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import unittest


def probability(weights, event):
    """Probability of an event in a finite explicitly normalized distribution."""
    if not weights or any(w < 0 for w in weights.values()):
        raise ValueError("invalid weights")
    if sum(weights.values(), F(0)) != 1:
        raise ValueError("weights must sum to 1")
    if not set(event) <= set(weights):
        raise ValueError("event outside the sample space")
    return sum((weights[x] for x in event), F(0))


def subsets(items):
    values = list(items)
    return [
        {values[i] for i in range(len(values)) if mask & (1 << i)}
        for mask in range(1 << len(values))
    ]


class ElementaryProbabilityTests(unittest.TestCase):
    def setUp(self):
        self.weights = {0: F(1, 10), 1: F(2, 10),
                        2: F(3, 10), 3: F(4, 10)}
        self.omega = set(self.weights)
        self.events = subsets(self.omega)

    def test_normalization_and_complement_exhaustive(self):
        self.assertEqual(probability(self.weights, set()), 0)
        self.assertEqual(probability(self.weights, self.omega), 1)
        for a in self.events:
            self.assertEqual(probability(self.weights, a) +
                             probability(self.weights, self.omega - a), 1)

    def test_inclusion_exclusion_and_union_bound_exhaustive(self):
        for a in self.events:
            for b in self.events:
                pa = probability(self.weights, a)
                pb = probability(self.weights, b)
                pab = probability(self.weights, a & b)
                pu = probability(self.weights, a | b)
                self.assertEqual(pu, pa + pb - pab)
                self.assertLessEqual(pu, pa + pb)
                self.assertGreaterEqual(pu, max(pa, pb))

    def test_monotonicity_and_difference_exhaustive(self):
        for a in self.events:
            for b in self.events:
                self.assertEqual(
                    probability(self.weights, a - b),
                    probability(self.weights, a) -
                    probability(self.weights, a & b))
                if a <= b:
                    self.assertLessEqual(probability(self.weights, a),
                                         probability(self.weights, b))

    def test_independence_complement(self):
        for a in self.events:
            for b in self.events:
                pa, pb = probability(self.weights, a), probability(self.weights, b)
                if probability(self.weights, a & b) == pa * pb:
                    self.assertEqual(
                        probability(self.weights, (self.omega-a) & b),
                        (1-pa)*pb)

    def test_disjoint_positive_not_independent(self):
        w = {i: F(1, 6) for i in range(1, 7)}
        a, b = {1}, {2}
        self.assertEqual(probability(w, a & b), 0)
        self.assertNotEqual(probability(w, a)*probability(w, b), 0)

    def test_coins_at_least_one_and_exactly_one(self):
        for n in range(1, 8):
            outcomes = list(product((0, 1), repeat=n))
            p = F(sum(any(x) for x in outcomes), len(outcomes))
            self.assertEqual(p, 1-F(1, 2)**n)
        for numerator in range(1, 6):
            p = F(numerator, 6)
            self.assertEqual(p*(1-p)+(1-p)*p, 2*p*(1-p))

    def test_dice(self):
        outcomes = list(product(range(1, 7), repeat=2))
        self.assertEqual(F(sum(i+j == 7 for i, j in outcomes), 36), F(1, 6))
        self.assertEqual(F(sum(i == 6 or j == 6 for i, j in outcomes), 36), F(11, 36))
        self.assertEqual(F(sum(i > j for i, j in outcomes), 36), F(5, 12))
        self.assertEqual(F(sum(i+j >= 11 for i, j in outcomes), 36), F(1, 12))

    def test_urn_without_replacement(self):
        self.assertEqual(F(3, 5)*F(2, 4), F(3, 10))
        self.assertEqual(1-F(2, 5)*F(1, 4), F(9, 10))
        self.assertEqual(F(4, 6)*F(3, 5)*F(2, 4), F(1, 5))
        for n in range(2, 12):
            for r in range(n+1):
                for draws in range(n+1):
                    from itertools import combinations
                    samples = list(combinations(range(n), draws))
                    observed = F(sum(all(x >= r for x in sample)
                                     for sample in samples), len(samples))
                    predicted = (F(comb(n-r, draws), comb(n, draws))
                                 if draws <= n-r else F(0))
                    self.assertEqual(observed, predicted)

    def test_total_probability_and_bayes(self):
        prior = F(1, 100)
        sensitivity = F(9, 10)
        false_positive = F(1, 10)
        positive = sensitivity*prior + false_positive*(1-prior)
        self.assertEqual(positive, F(108, 1000))
        self.assertEqual(sensitivity*prior/positive, F(1, 12))

    def test_expectation_linearity_dependent(self):
        # Y=2X is fully dependent on X.
        weights = {0: F(1, 3), 1: F(2, 3)}
        def expect(fn):
            return sum((fn(x)*w for x, w in weights.items()), F(0))
        self.assertEqual(expect(lambda x: 3*x+2*(2*x)),
                         3*expect(lambda x: x)+2*expect(lambda x: 2*x))
        self.assertEqual(sum((F(1, d) for d in (2, 3, 4, 5)), F(0)), F(77, 60))

    def test_specific_solutions(self):
        self.assertEqual(F(4+13-1, 52), F(4, 13))
        self.assertEqual(F(4, 52)*F(3, 51), F(1, 221))
        self.assertEqual(1-F(95, 100)*F(94, 99), F(97, 990))
        self.assertEqual(1-F(6, 10)*F(5, 9)*F(4, 8), F(5, 6))
        self.assertEqual(F(18+14-6, 30), F(13, 15))

    def test_invalid_probability_inputs(self):
        with self.assertRaises(ValueError):
            probability({1: F(1, 2)}, {1})
        with self.assertRaises(ValueError):
            probability({1: F(-1), 2: F(2)}, {1})
        with self.assertRaises(ValueError):
            probability({1: F(1)}, {2})


if __name__ == "__main__":
    unittest.main()
