import unittest
from fractions import Fraction as F
from itertools import product

def d(a,k):
    return a*(F(1,k**5)-F(1,(k+1)**5))

def greedy(a,N):
    n=[1]*len(a)
    for _ in range(N-len(a)):
        j=max(range(len(a)),key=lambda j:(d(a[j],n[j]),-j))
        n[j]+=1
    return tuple(n)

def allocations(r,N):
    if r==1:
        yield (N,)
    else:
        for x in range(1,N-r+2):
            for tail in allocations(r-1,N-x):
                yield (x,)+tail

def cost(a,n):
    return sum((a[j]/n[j]**5 for j in range(len(a))),F(0))

class GOTests(unittest.TestCase):
    def test_exhaustive(self):
        count=0
        for r in (2,3):
            for a in product((F(1),F(2),F(3)),repeat=r):
                for N in range(r,r+7):
                    n=greedy(a,N)
                    vals=[cost(a,x) for x in allocations(r,N)]
                    self.assertEqual(cost(a,n),min(vals))
                    count+=1
        self.assertEqual(count,252)
    def test_nested_and_diminishing(self):
        for a in ((F(1),F(1)),(F(2),F(3),F(1))):
            ns=[greedy(a,N) for N in range(len(a),len(a)+12)]
            for p,q in zip(ns,ns[1:]):
                self.assertEqual(sum(q)-sum(p),1)
                self.assertTrue(all(y>=x for x,y in zip(p,q)))
            savings=[cost(a,p)-cost(a,q) for p,q in zip(ns,ns[1:])]
            self.assertEqual(savings,sorted(savings,reverse=True))
    def test_second_best(self):
        for a in product((F(1),F(2),F(3)),repeat=3):
            for N in range(4,10):
                n=greedy(a,N)
                vals={x:cost(a,x) for x in allocations(3,N)}
                other=min(v for x,v in vals.items() if x!=n)
                delta=min(d(a[i],n[i]-1)-d(a[j],n[j]) for i in range(3) if n[i]>1 for j in range(3) if i!=j)
                self.assertEqual(other-vals[n],delta)

if __name__=="__main__":
    unittest.main()
