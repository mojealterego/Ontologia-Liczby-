import itertools
import unittest
from fractions import Fraction as F

def allocations(r,N):
    return [v for v in itertools.product(range(1,N+1),repeat=r) if sum(v)==N]

def value(a,n):
    return sum((x/F(k**5) for x,k in zip(a,n)),F(0))

def local(a,n):
    r=len(n)
    for i in range(r):
        if n[i]<2: continue
        for j in range(r):
            if i==j: continue
            v=list(n);v[i]-=1;v[j]+=1
            if value(a,n)>value(a,v):return False
    return True

class TestGM(unittest.TestCase):
    def test_exchange_exhaustive(self):
        for r in (2,3):
            for N in range(r,9):
                for a in itertools.product((F(1),F(2),F(5)),repeat=r):
                    ns=allocations(r,N);best=min(value(a,n) for n in ns)
                    for n in ns:self.assertEqual(local(a,n),value(a,n)==best)
    def test_robust_endpoints(self):
        a=(F(2),F(1));e=(F(1,4),F(1,4));n=(2,1)
        self.assertTrue(all(value(b,n)==min(value(b,v) for v in allocations(2,3)) for b in itertools.product(*[(x-y,x+y) for x,y in zip(a,e)])))
    def test_regret(self):
        for a in itertools.product((F(1),F(2),F(4)),repeat=2):
            b=tuple(x+F(1,10) for x in a)
            ns=allocations(2,5)
            na=min(ns,key=lambda n:value(a,n));nb=min(ns,key=lambda n:value(b,n))
            self.assertLessEqual(value(a,nb)-value(a,na),F(2,5))
if __name__=="__main__":unittest.main()
