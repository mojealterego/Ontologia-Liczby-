"""Regression tests for F28.2-GL; exact rational arithmetic."""
from fractions import Fraction
from itertools import product
import unittest

def score(a, n):
    return sum((Fraction(x, k**5) for x, k in zip(a, n)), Fraction())

def greedy(a, N):
    r = len(a)
    if N < r or not r or any(x < 0 for x in a):
        raise ValueError("invalid allocation")
    n = [1] * r
    for _ in range(N-r):
        j = max(range(r), key=lambda j: (Fraction(a[j], n[j]**5)-Fraction(a[j], (n[j]+1)**5), -j))
        n[j] += 1
    return tuple(n)

def allocations(r, N):
    if r == 1:
        yield (N,)
    else:
        for k in range(1, N-r+2):
            for tail in allocations(r-1, N-k):
                yield (k,) + tail

class IntegerAllocationTests(unittest.TestCase):
    def test_exhaustive_global_optimality(self):
        cases = 0
        for r in (1,2,3,4):
            for N in range(r, min(r+6, 10)):
                for a in product((0,1,4,16), repeat=r):
                    g = greedy(a, N)
                    self.assertEqual(sum(g), N)
                    self.assertEqual(score(a,g), min(score(a,n) for n in allocations(r,N)))
                    cases += 1
        self.assertGreater(cases, 1000)

    def test_examples(self):
        self.assertEqual(greedy((1,64),4),(1,3))
        self.assertEqual(score((1,64),(1,3)),Fraction(307,243))
        self.assertEqual(greedy((0,8),5),(1,4))
        self.assertEqual(score((0,8),(1,4)),Fraction(1,128))
        self.assertEqual(score((1,1,1),(2,2,1)),Fraction(17,16))

    def test_marginal_decrease(self):
        for a in (0,1,4,64):
            values = [Fraction(a,k**5)-Fraction(a,(k+1)**5) for k in range(1,20)]
            self.assertTrue(all(x>=y>=0 for x,y in zip(values,values[1:])))

if __name__ == "__main__":
    unittest.main()
