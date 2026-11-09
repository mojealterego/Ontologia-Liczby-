"""Exact rational test of F28.2-HF dual certificate."""
from fractions import Fraction as F
from itertools import product
import unittest

def vertices(lo, hi):
    n=len(lo); out=set()
    for free in range(n):
        other=[j for j in range(n) if j!=free]
        for vals in product(*[(lo[j],hi[j]) for j in other]):
            u=[None]*n
            for j,x in zip(other,vals): u[j]=x
            u[free]=-sum(vals)
            if lo[free]<=u[free]<=hi[free]: out.add(tuple(u))
    return out

def certified(u,lo,hi,d):
    lower=upper=None
    for x,l,h,c in zip(u,lo,hi,d):
        if l==h: continue
        if x==h: lower=c if lower is None else max(lower,c)
        elif x==l: upper=c if upper is None else min(upper,c)
        else:
            lower=c if lower is None else max(lower,c)
            upper=c if upper is None else min(upper,c)
    return lower is None or upper is None or lower<=upper

class TestHF(unittest.TestCase):
    def test_exact_certificate(self):
        count=0
        for n in (2,3):
            for d in product((-2,0,2),repeat=n):
                for lows in product((-1,0),repeat=n):
                    lo=tuple(map(F,lows)); hi=tuple(x+1 for x in lo)
                    vv=vertices(lo,hi)
                    if not vv: continue
                    opt=min(sum(c*x for c,x in zip(d,v)) for v in vv)
                    for v in vv:
                        self.assertEqual(certified(v,lo,hi,d),sum(c*x for c,x in zip(d,v))==opt)
                        count+=1
        self.assertEqual(count,594)

    def test_examples(self):
        self.assertEqual(min(sum(c*x for c,x in zip((3,1,2),v)) for v in vertices((F(-1),)*3,(F(1),)*3)),-2)
        self.assertEqual(min(sum(c*x for c,x in zip((1,1,3),v)) for v in vertices((F(0),F(0),F(-2)),(F(2),F(2),F(0)))),-4)

if __name__=="__main__": unittest.main()
