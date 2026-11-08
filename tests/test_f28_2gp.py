from fractions import Fraction as F
from itertools import product
import unittest

def allocations(r,N):
    if r==1:
        yield (N,)
    else:
        for k in range(1,N-r+2):
            for t in allocations(r-1,N-k):
                yield (k,)+t

def cost(a,n):
    return sum((x/F(k**5) for x,k in zip(a,n)),F(0))

def greedy(a,N):
    n=[1]*len(a)
    for _ in range(N-len(a)):
        j=max(range(len(a)),key=lambda i:(a[i]*(F(1,n[i]**5)-F(1,(n[i]+1)**5)),-i))
        n[j]+=1
    return tuple(n)

def robust(lo,hi,n):
    return all(lo[i]*(F(1,(n[i]-1)**5)-F(1,n[i]**5)) >=
               hi[j]*(F(1,n[j]**5)-F(1,(n[j]+1)**5))
               for i in range(len(n)) if n[i]>1 for j in range(len(n)) if i!=j)

class TestGP(unittest.TestCase):
    def test_robust_certificates(self):
        count=0
        for r in (2,3):
            for N in range(r+1,r+5):
                for lo in product((F(1),F(2)),repeat=r):
                    hi=tuple(x+F(1,2) for x in lo)
                    for n in allocations(r,N):
                        cert=robust(lo,hi,n)
                        actual=all(cost(a,n)==min(cost(a,m) for m in allocations(r,N))
                                   for a in product(*[(lo[i],hi[i]) for i in range(r)]))
                        self.assertEqual(cert,actual)
                        count+=1
        self.assertGreater(count,100)
    def test_regret(self):
        for a in product((F(1),F(3)),repeat=3):
            for b in product((F(1),F(2)),repeat=3):
                n=greedy(b,7)
                opt=min(cost(a,m) for m in allocations(3,7))
                self.assertLessEqual(cost(a,n)-opt,2*sum(abs(x-y) for x,y in zip(a,b)))
    def test_nonrobust(self):
        self.assertNotEqual(cost((F(1),F(4)),(2,1)),min(cost((F(1),F(4)),m) for m in allocations(2,3)))

if __name__=='__main__':
    unittest.main()
