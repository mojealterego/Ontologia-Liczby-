from fractions import Fraction as Q
from itertools import product
import unittest

def alloc(r,N):
    if r==1:
        if N>=1: yield (N,)
    else:
        for k in range(1,N-r+2):
            for t in alloc(r-1,N-k): yield (k,)+t

def d(k): return Q(1,k**5)-Q(1,(k+1)**5)
def cost(a,n): return sum((a[i]/n[i]**5 for i in range(len(n))),Q(0))
def criterion(a,n):
    return all(a[i]*d(n[i]-1)>=a[j]*d(n[j]) for i in range(len(n)) if n[i]>1 for j in range(len(n)) if i!=j)

class TestF282GQ(unittest.TestCase):
    def test_optimality(self):
        cases=0
        for r in (2,3):
            for N in range(r,r+5):
                ns=list(alloc(r,N))
                for aa in product((1,2,3),repeat=r):
                    a=tuple(map(Q,aa))
                    best=min(cost(a,n) for n in ns)
                    for n in ns:
                        self.assertEqual(criterion(a,n),cost(a,n)==best)
                        cases+=1
        self.assertEqual(cases,1080)

    def test_unique_and_ties(self):
        ns=list(alloc(2,3))
        for a,expected in [((Q(3),Q(1)),1),((Q(1),Q(1)),2)]:
            values=[cost(a,n) for n in ns]
            self.assertEqual(values.count(min(values)),expected)

    def test_value_lipschitz(self):
        ns=list(alloc(3,6))
        for aa in product((1,2,3),repeat=3):
            a=tuple(map(Q,aa))
            b=tuple(x+Q(1,3) for x in a)
            self.assertLessEqual(abs(min(cost(a,n) for n in ns)-min(cost(b,n) for n in ns)),sum(abs(x-y) for x,y in zip(a,b)))

if __name__=="__main__": unittest.main()
