"""Exact rational regression for F28.2-GS."""
from fractions import Fraction as Q
from itertools import product
import unittest

def allocations(r, N):
    return (p for p in product(range(1, N+1), repeat=r) if sum(p)==N)

def value(a, n):
    return sum((x / (k**5) for x,k in zip(a,n)), Q(0))

def greedy(a, N):
    n=[1]*len(a)
    for _ in range(N-len(a)):
        j=max(range(len(a)),key=lambda i:(a[i]*(Q(1,n[i]**5)-Q(1,(n[i]+1)**5)),-i))
        n[j]+=1
    return tuple(n)

class ExactChecks(unittest.TestCase):
    def test_global_optimum(self):
        count=0
        for r in (2,3):
            for N in range(r,r+6):
                for w in product((1,2,3),repeat=r):
                    a=tuple(map(Q,w))
                    g=greedy(a,N)
                    self.assertEqual(value(a,g),min(value(a,n) for n in allocations(r,N)))
                    count+=1
        self.assertEqual(count,216)

    def test_own_weight_monotonicity(self):
        count=0
        for r in (2,3):
            for N in range(r,r+6):
                for w in product((1,2,3),repeat=r):
                    a=tuple(map(Q,w))
                    for i in range(r):
                        b=list(a); b[i]+=Q(1,2)
                        self.assertGreaterEqual(greedy(b,N)[i],greedy(a,N)[i])
                        count+=1
        self.assertEqual(count,594)

    def test_examples(self):
        self.assertEqual(greedy((Q(2),Q(1)),3),(2,1))
        self.assertEqual(value((Q(2),Q(1)),(2,1)),Q(17,16))
        self.assertEqual(value((Q(1),Q(1)),(2,1)),Q(33,32))
        self.assertEqual(greedy((Q(1),Q(1)),4),(2,2))
        self.assertEqual(Q(1,2**5)-Q(1,3**5),Q(211,7776))

if __name__=="__main__":
    unittest.main()
