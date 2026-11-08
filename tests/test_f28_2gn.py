import unittest
from fractions import Fraction as F
from itertools import product

def allocations(r,N):
    if r==1:
        yield (N,)
    else:
        for k in range(1,N-r+2):
            for tail in allocations(r-1,N-k):
                yield (k,)+tail

def val(a,n):
    return sum((x/F(k**5) for x,k in zip(a,n)),F(0))

def delta(a,k):
    return a*(F(1,k**5)-F(1,(k+1)**5))

def gap(a,n):
    L=min(delta(a[j],n[j]-1) for j in range(len(n)) if n[j]>1)
    U=max(delta(a[j],n[j]) for j in range(len(n)))
    return L-U

class TestGN(unittest.TestCase):
    def test_exhaustive_gap(self):
        count=0
        for r in (2,3):
            for N in range(r+1,r+6):
                for a in product((F(1),F(2),F(3)),repeat=r):
                    vals=sorted((val(a,n),n) for n in allocations(r,N))
                    minimum=vals[0][0]
                    for n in allocations(r,N):
                        g=gap(a,n)
                        self.assertEqual(g>=0,val(a,n)==minimum)
                        self.assertEqual(g>0,sum(val(a,m)==minimum for m in allocations(r,N))==1 and val(a,n)==minimum)
                        if g>0:
                            self.assertEqual(min(val(a,m)-minimum for m in allocations(r,N) if m!=n),g)
                        count+=1
        print('exact enumeration cases',count)
    def test_examples(self):
        self.assertEqual(gap((F(2),F(1)),(2,1)),F(31,32))
        self.assertEqual(gap((F(1),F(1)),(2,2)),F(7322,7776))
        self.assertEqual(gap((F(1),F(1)),(2,1)),0)
    def test_robust(self):
        a=(F(2),F(1));e=(F(1,4),F(1,4));n=(2,1)
        for b in product(*[(a[j]-e[j],a[j]+e[j]) for j in range(2)]):
            self.assertGreater(gap(b,n),0)

if __name__=='__main__': unittest.main()
