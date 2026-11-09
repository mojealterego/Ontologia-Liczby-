"""Exact rational regression for F28.2-HE; run: python -m unittest tests/test_f28_2he.py"""
import itertools
import unittest
from fractions import Fraction as Q

def dual(d,l,h):
    return max(sum(min((dj-dk)*lj,(dj-dk)*hj) for dj,lj,hj in zip(d,l,h)) for dk in d)

def vertices(d,l,h):
    n=len(d); vals=[]
    for free in range(n):
        for ends in itertools.product((0,1),repeat=n-1):
            u=[None]*n
            it=iter(ends)
            for j in range(n):
                if j!=free:
                    u[j]=(l[j],h[j])[next(it)]
            u[free]=-sum(x for x in u if x is not None)
            if l[free]<=u[free]<=h[free]:
                vals.append(sum(x*y for x,y in zip(d,u)))
    return min(vals)

class TestHE(unittest.TestCase):
    def test_duality_exhaustive(self):
        count=0
        for n in (2,3):
            for d in itertools.product((-2,0,3),repeat=n):
                for lows in itertools.product((1,2),repeat=n):
                    for highs in itertools.product((1,2),repeat=n):
                        l=tuple(Q(-x) for x in lows)
                        h=tuple(Q(x) for x in highs)
                        dd=tuple(Q(x) for x in d)
                        self.assertEqual(dual(dd,l,h),vertices(dd,l,h))
                        count+=1
        self.assertEqual(count,1872)

if __name__=="__main__":
    unittest.main()
