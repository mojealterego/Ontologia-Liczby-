"""Exact finite checks for MSC 97C30; not a formal proof or empirical validation."""
from fractions import Fraction as F
from itertools import combinations
from math import exp, isclose, log, log2
import unittest


EDGES = (("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"))
V = frozenset("abcd")


def closure(nodes, edges=EDGES):
    result = set(nodes)
    while True:
        before = len(result)
        result.update(u for u, v in edges if v in result)
        if len(result) == before:
            return frozenset(result)


def ideals(edges=EDGES, vertices=V):
    return [frozenset(s) for n in range(len(vertices) + 1)
            for s in combinations(sorted(vertices), n)
            if closure(s, edges) == frozenset(s)]


def posterior_positive(p, s, t):
    return s*p / (s*p+(1-t)*(1-p))


def posterior_negative(p, s, t):
    return (1-s)*p / ((1-s)*p+t*(1-p))


def markov_step(p, learning, forgetting):
    return (1-learning-forgetting)*p+learning


def sigma(x):
    return 1/(1+exp(-x))


def entropy(p):
    if p in (0, 1):
        return 0.0
    return -p*log2(p)-(1-p)*log2(1-p)


class CognitiveMathematicsTests(unittest.TestCase):
    def test_z01_closure(self):
        self.assertEqual(closure({'d'}), V)

    def test_z02_chain_ideals(self):
        self.assertEqual(len(ideals((('a','b'),('b','c')), frozenset('abc'))), 4)

    def test_z03_topological(self):
        for order in ('abcd','acbd'):
            position = {v: i for i, v in enumerate(order)}
            self.assertTrue(all(position[u] < position[v] for u,v in EDGES))

    def test_z04_incremental_cost(self):
        self.assertEqual(len(closure({'d'}) - {'a','b'}), 2)

    def test_z05_lattice(self):
        m,n = frozenset('ab'), frozenset('ac')
        self.assertEqual(m|n, frozenset('abc'))
        self.assertEqual(m&n, frozenset('a'))
        self.assertIn(m|n, ideals())
        self.assertIn(m&n, ideals())

    def test_t01_closure_operator_exhaustive(self):
        subsets = [frozenset(s) for k in range(5) for s in combinations(sorted(V),k)]
        for a in subsets:
            self.assertTrue(a <= closure(a))
            self.assertEqual(closure(closure(a)), closure(a))
            for b in subsets:
                if a <= b:
                    self.assertTrue(closure(a) <= closure(b))

    def test_t02_ideals_closed_exhaustive(self):
        all_ideals = ideals()
        for m in all_ideals:
            for n in all_ideals:
                self.assertIn(m|n, all_ideals)
                self.assertIn(m&n, all_ideals)

    def test_t05_cost_monotonicity_exhaustive(self):
        for m in ideals():
            for n in ideals():
                if m <= n:
                    for v in V:
                        self.assertLessEqual(len(closure({v})-n),len(closure({v})-m))

    def test_z06_bayes_positive(self):
        self.assertEqual(posterior_positive(F(1,4),F(4,5),F(9,10)),F(8,11))

    def test_z07_bayes_negative(self):
        self.assertEqual(posterior_negative(F(1,4),F(4,5),F(9,10)),F(2,29))

    def test_z08_odds(self):
        prior_odds=F(1,3)
        likelihood_ratio=F(4,5)/F(1,10)
        self.assertEqual(prior_odds*likelihood_ratio,F(8,3))

    def test_z09_two_independent_successes(self):
        odds=F(1,3)*(F(4,5)/F(1,10))**2
        self.assertEqual(odds/(1+odds),F(64,67))

    def test_z10_predictive_probability(self):
        p,s,t=F(1,4),F(4,5),F(9,10)
        self.assertEqual(s*p+(1-t)*(1-p),F(11,40))

    def test_t08_positive_evidence_condition(self):
        p=F(2,5)
        for s,t in [(F(4,5),F(9,10)),(F(1,5),F(1,5)),(F(1,2),F(1,2))]:
            self.assertEqual(posterior_positive(p,s,t)>p,s>1-t)

    def test_k06_low_base_rate(self):
        self.assertEqual(posterior_positive(F(1,100),F(9,10),F(9,10)),F(1,12))

    def test_z11_stationary_probability(self):
        l,f=F(1,5),F(1,10)
        p=l/(l+f)
        self.assertEqual(p,F(2,3))
        self.assertEqual(markov_step(p,l,f),p)

    def test_z12_one_markov_step(self):
        self.assertEqual(markov_step(F(1,3),F(1,5),F(1,10)),F(13,30))

    def test_z13_two_markov_steps(self):
        p=F(1,3)
        for _ in range(2):
            p=markov_step(p,F(1,5),F(1,10))
        self.assertEqual(p,F(151,300))

    def test_t11_markov_closed_form(self):
        l,f,p0=F(1,5),F(1,10),F(1,3)
        fixed=l/(l+f)
        p=p0
        for n in range(15):
            self.assertEqual(p-fixed,(1-l-f)**n*(p0-fixed))
            p=markov_step(p,l,f)

    def test_z14_retention(self):
        self.assertTrue(isclose(exp(-(log(2)/4)*8),1/4,rel_tol=1e-14))

    def test_z15_equal_spacing(self):
        self.assertEqual(sum((4,4,4)),12)
        self.assertEqual(max((4,4,4)),4)
        for a in range(1,12):
            for b in range(1,12-a):
                c=12-a-b
                self.assertGreaterEqual(max(a,b,c),4)

    def test_z16_load(self):
        self.assertEqual(6+4,10)
        self.assertGreater(6+5+4,10)

    def test_z17_knapsack_counterexample(self):
        self.assertEqual(5+5,10)
        self.assertGreater(8+8,9)

    def test_z18_logistic_midpoint(self):
        self.assertEqual(sigma(0),0.5)

    def test_z19_logistic_log_three(self):
        self.assertTrue(isclose(sigma(log(3)),3/4,rel_tol=1e-14))

    def test_t15_logistic_symmetry_and_bound(self):
        for x in (-10,-3,-1,0,1,3,10):
            p=sigma(x)
            self.assertTrue(isclose(sigma(-x),1-p,abs_tol=1e-14))
            self.assertLessEqual(p*(1-p),0.25)

    def test_z20_entropy(self):
        self.assertEqual(entropy(0.5),1)
        self.assertEqual(entropy(1),0)

    def test_t16_entropy_bound(self):
        for k in range(101):
            h=entropy(k/100)
            self.assertGreaterEqual(h,0)
            self.assertLessEqual(h,1)


if __name__ == '__main__':
    unittest.main()
