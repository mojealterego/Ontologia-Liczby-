"""Finite-model verification for MSC 97D40 III-I.

Exhaustive rational-grid properties and exact boundary cases. These are model
checks, not empirical validation of educational effectiveness.
"""
import itertools
import math
import unittest
from fractions import Fraction


def transition(a, r, p):
    return a + (r - a) * p


def iterate(a, r, p, t):
    for _ in range(t):
        p = transition(a, r, p)
    return p


def frontier(nodes, edges, mastered):
    return {v for v in nodes - mastered if all(u in mastered for u, w in edges if w == v)}


def closed(edges, mastered):
    return all(u in mastered for u, v in edges if v in mastered)


class MasteryModelTests(unittest.TestCase):
    def test_transition_preserves_unit_interval(self):
        grid = [Fraction(i, 5) for i in range(6)]
        for a, r, p in itertools.product(grid, repeat=3):
            self.assertTrue(0 <= transition(a, r, p) <= 1)

    def test_closed_form_exact(self):
        grid = [Fraction(i, 4) for i in range(5)]
        for a, r, p in itertools.product(grid, repeat=3):
            lam = r - a
            for t in range(9):
                expected = lam**t * p + a * sum((lam**j for j in range(t)), Fraction(0))
                self.assertEqual(iterate(a, r, p, t), expected)

    def test_stationary_exact(self):
        grid = [Fraction(i, 5) for i in range(6)]
        for a, r in itertools.product(grid, repeat=2):
            if (a, r) == (0, 1):
                continue
            stationary = a / (1 - r + a)
            self.assertEqual(transition(a, r, stationary), stationary)
            self.assertTrue(0 <= stationary <= 1)

    def test_boundary_oscillation_and_identity(self):
        p = Fraction(2, 7)
        self.assertEqual([iterate(0, 1, p, t) for t in range(6)], [p] * 6)
        self.assertEqual([iterate(1, 0, p, t) for t in range(6)], [p, 1-p] * 3)

    def test_contraction_exact(self):
        grid = [Fraction(i, 4) for i in range(5)]
        for a, r, p, q in itertools.product(grid, repeat=4):
            for t in range(5):
                self.assertEqual(abs(iterate(a, r, p, t) - iterate(a, r, q, t)),
                                 abs(r-a)**t * abs(p-q))

    def test_action_dominance(self):
        grid = [Fraction(i, 4) for i in range(5)]
        for a0, a1, r0, r1, p in itertools.product(grid, repeat=5):
            if a1 >= a0 and r1 >= r0:
                self.assertGreaterEqual(transition(a1, r1, p), transition(a0, r0, p))

    def test_parameter_sensitivity(self):
        grid = [Fraction(i, 4) for i in range(5)]
        for a0, a1, r0, r1, p in itertools.product(grid, repeat=5):
            self.assertLessEqual(abs(transition(a1, r1, p)-transition(a0, r0, p)),
                                 max(abs(a1-a0), abs(r1-r0)))

    def test_perturbation_bound(self):
        grid = [Fraction(i, 4) for i in range(5)]
        for a1, r1, a0, r0 in itertools.product(grid, repeat=4):
            c = abs(r1-a1)
            if c == 1:
                continue
            eps = max(abs(a1-a0), abs(r1-r0))
            for t in range(6):
                p = Fraction(2, 5)
                actual = abs(iterate(a1, r1, p, t) - iterate(a0, r0, p, t))
                self.assertLessEqual(actual, eps * (1-c**t)/(1-c))

    def test_exponential_semigroup_and_half_life(self):
        for k in (0, .1, .5, 1.0):
            for d, e in itertools.product(range(6), repeat=2):
                self.assertAlmostEqual(math.exp(-k*(d+e)), math.exp(-k*d)*math.exp(-k*e))
        for k in (.1, .5, 1.0):
            self.assertAlmostEqual(math.exp(-k*(math.log(2)/k)), .5)

    def test_frontier_preserves_closure(self):
        nodes = set(range(4))
        positions = [(i,j) for i in range(4) for j in range(i+1,4)]
        for mask in range(1 << len(positions)):
            edges = {edge for i,edge in enumerate(positions) if mask & (1<<i)}
            for smask in range(1 << 4):
                mastered = {i for i in nodes if smask & (1<<i)}
                if closed(edges, mastered):
                    for v in frontier(nodes, edges, mastered):
                        self.assertTrue(closed(edges, mastered | {v}))

    def test_frontier_reaches_full_dag(self):
        nodes = set(range(4))
        positions = [(i,j) for i in range(4) for j in range(i+1,4)]
        for mask in range(1 << len(positions)):
            edges = {edge for i,edge in enumerate(positions) if mask & (1<<i)}
            mastered = set()
            while mastered != nodes:
                available = frontier(nodes, edges, mastered)
                self.assertTrue(available)
                mastered.add(min(available))
                self.assertTrue(closed(edges, mastered))

    def test_beta_posterior_predictive(self):
        for alpha, beta, s, f in itertools.product(range(1,5), range(1,5), range(5), range(5)):
            posterior_mean = Fraction(alpha+s, alpha+beta+s+f)
            if s+f:
                weighted = (Fraction(alpha+beta, alpha+beta+s+f) * Fraction(alpha,alpha+beta)
                            + Fraction(s+f, alpha+beta+s+f) * Fraction(s,s+f))
                self.assertEqual(posterior_mean, weighted)
            self.assertTrue(0 < posterior_mean < 1)

    def test_test_identifiability(self):
        grid = [Fraction(i, 5) for i in range(6)]
        for se, sp, p in itertools.product(grid, repeat=3):
            q = se*p + (1-sp)*(1-p)
            if se+sp != 1:
                self.assertEqual((q+sp-1)/(se+sp-1), p)
            else:
                self.assertEqual(q, 1-sp)

    def test_worked_examples(self):
        self.assertEqual(transition(Fraction(1,5), Fraction(9,10), Fraction(2,5)), Fraction(12,25))
        self.assertEqual(iterate(Fraction(1,5), Fraction(9,10), Fraction(2,5),2),Fraction(67,125))
        self.assertEqual(Fraction(1,5)/(1-Fraction(9,10)+Fraction(1,5)),Fraction(2,3))
        self.assertEqual(Fraction(5,9),Fraction(2+3,2+3+3+1))
        self.assertEqual(Fraction(9,10)*Fraction(3,5)+Fraction(1,5)*Fraction(2,5),Fraction(31,50))


if __name__ == '__main__':
    unittest.main()
