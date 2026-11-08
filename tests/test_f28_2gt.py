from fractions import Fraction as Q
from itertools import product
from unittest import TestCase, main

def allocate(weights, budget):
    n=[1]*len(weights)
    for _ in range(budget-len(weights)):
        j=max(range(len(n)), key=lambda i:(weights[i]*(Q(1,n[i]**5)-Q(1,(n[i]+1)**5)), -i))
        n[j]+=1
    return tuple(n)

def cost(w,n):
    return sum((w[i]/n[i]**5 for i in range(len(n))),Q(0))

def compositions(total,r):
    if r==1:
        yield (total,); return
    for x in range(1,total-r+2):
        for rest in compositions(total-x,r-1): yield (x,)+rest

class Tests(TestCase):
    def test_optimality(self):
        for r in (2,3):
            for weights in product((Q(1),Q(2),Q(4)),repeat=r):
                for budget in range(r,r+6):
                    n=allocate(weights,budget)
                    self.assertEqual(cost(weights,n),min(cost(weights,m) for m in compositions(budget,r)))
    def test_cross_monotonicity(self):
        for r in (2,3):
            for weights in product((Q(1),Q(2),Q(4)),repeat=r):
                for budget in range(r,r+6):
                    for i in range(r):
                        w=list(weights); w[i]*=Q(3,2)
                        a=allocate(weights,budget); b=allocate(w,budget)
                        self.assertGreaterEqual(b[i],a[i])
                        for j in range(r):
                            if j!=i:self.assertLessEqual(b[j],a[j])
    def test_value_bounds(self):
        for w in product((Q(1),Q(2),Q(4)),repeat=3):
            n=allocate(w,7)
            for i in range(3):
                v=list(w);v[i]+=Q(1,3)
                old=cost(w,n); new=cost(v,allocate(v,7))
                self.assertTrue(0<=new-old<=Q(1,3))
if __name__=='__main__':main()
