"""Exact rational arithmetic tests for F28.2-B. Finite checks are not proofs."""
from fractions import Fraction as Q
from itertools import product
import unittest

def soft(y: Q, lam: Q) -> Q:
    if lam < 0:
        raise ValueError("lambda must be nonnegative")
    return max(y - lam, Q(0)) if y >= 0 else min(y + lam, Q(0))

def project(x: Q, lo: Q, hi: Q) -> Q:
    if lo > hi:
        raise ValueError("empty interval")
    return min(hi, max(lo, x))

def objective(x: Q, y: Q, lam: Q) -> Q:
    return (x-y)**2 / 2 + lam * abs(x)

def subgrad_interval(x: Q, y: Q, lam: Q) -> tuple[Q, Q]:
    if x < 0:
        return x-y-lam, x-y-lam
    if x > 0:
        return x-y+lam, x-y+lam
    return -y-lam, -y+lam

class F282BNonsmooth(unittest.TestCase):
    def test_exact_examples(self):
        self.assertEqual(soft(Q(3), Q(1)), Q(2))
        self.assertEqual(soft(Q(1,2), Q(1)), Q(0))
        self.assertEqual(soft(Q(-5,2), Q(3,2)), Q(-1))
        self.assertEqual(project(soft(Q(3), Q(1)), Q(-1), Q(1)), Q(1))
        self.assertEqual(subgrad_interval(Q(0), Q(3), Q(1)), (Q(-4), Q(-2)))
        self.assertEqual(subgrad_interval(Q(0), Q(-2), Q(1)), (Q(1), Q(3)))

    def test_necessary_and_sufficient_stationarity_enumerated(self):
        for y, lam in product((Q(k,2) for k in range(-12,13)), (Q(k,2) for k in range(0,9))):
            s = soft(y, lam)
            low, high = subgrad_interval(s, y, lam)
            self.assertLessEqual(low, 0)
            self.assertGreaterEqual(high, 0)
            for x in (Q(k,2) for k in range(-12,13)):
                self.assertGreaterEqual(objective(x,y,lam), objective(s,y,lam))

    def test_stability_data_and_threshold(self):
        values = [Q(k,2) for k in range(-10,11)]
        thresholds = [Q(k,2) for k in range(0,7)]
        for lam in thresholds:
            for y,z in product(values,repeat=2):
                self.assertLessEqual(abs(soft(y,lam)-soft(z,lam)),abs(y-z))
        for y in values:
            for lam,mu in product(thresholds,repeat=2):
                self.assertLessEqual(abs(soft(y,lam)-soft(y,mu)),abs(lam-mu))

    def test_projection_and_constrained_optimality(self):
        for y in [Q(k,2) for k in range(-6,7)]:
            for lam in [Q(0),Q(1,2),Q(1),Q(2)]:
                for lo,hi in ((Q(-1),Q(1)),(Q(0),Q(1)),(Q(1),Q(1))):
                    s = project(soft(y,lam),lo,hi)
                    for x in [lo+(hi-lo)*Q(i,12) for i in range(13)]:
                        self.assertGreaterEqual(objective(x,y,lam),objective(s,y,lam))

    def test_gap_and_subgradient_error_bound(self):
        for y in [Q(k,2) for k in range(-8,9)]:
            for lam in [Q(0),Q(1,2),Q(1),Q(2)]:
                s = soft(y,lam)
                for x in [Q(k,2) for k in range(-8,9)]:
                    gap=objective(x,y,lam)-objective(s,y,lam)
                    self.assertGreaterEqual(gap,(x-s)**2/2)
                    lo,hi=subgrad_interval(x,y,lam)
                    for g in (lo,hi):
                        self.assertLessEqual(gap,g*g/2)
                        self.assertLessEqual(abs(x-s),abs(g))

    def test_counterexamples(self):
        self.assertEqual(soft(Q(1,2),Q(1)),Q(0))
        self.assertNotEqual(Q(1,2)-Q(1),soft(Q(1,2),Q(1)))
        self.assertEqual(abs(soft(Q(3),Q(1))-soft(Q(4),Q(1))),Q(1))
        self.assertEqual(project(soft(Q(-2),Q(1)),Q(0),Q(1)),Q(0))
        lo,hi=subgrad_interval(Q(0),Q(-2),Q(1))
        self.assertGreater(lo,0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError): soft(Q(2),Q(-1))
        with self.assertRaises(ValueError): project(Q(2),Q(3),Q(1))

if __name__ == "__main__":
    unittest.main()
