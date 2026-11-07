#!/usr/bin/env python3
"""Exact Fraction regression for F28.2-FJ; no external dependencies."""
from fractions import Fraction as F
from itertools import product
def run(x, a):
    p=F(1); energy=x*x; checks=0
    for t in a:
        nxt=p*(1-t)
        assert p*p*energy-nxt*nxt*energy==t*(2-t)*p*p*energy
        checks+=1; p=nxt
    assert p==__import__('functools').reduce(lambda v,t:v*(1-t),a,F(1))
    return p,checks+1
def main():
    checks=0
    for x in (F(-3),F(0),F(2),F(5,2)):
        for a in product((F(0),F(1,4),F(1,2),F(1),F(3,2),F(2),F(3)),repeat=3):
            p,n=run(x,a);checks+=n
            if x:
                assert (p==0)==(F(1) in a);checks+=1
    for a,b in product((F(0),F(1,2),F(1),F(3,2)),repeat=2):
        for c,d in product((F(0),F(1,2),F(1),F(3,2)),repeat=2):
            lhs=(1-a)*(1-b)-(1-c)*(1-d)
            rhs=(c-a)*(1-b)+(d-b)*(1-c)
            assert lhs==rhs;checks+=1
    assert F(3,4)**4*8==F(81,32)
    assert F(9)-F(9,81)==F(80,9)
    assert F(1,4)+F(7,40)==F(17,40)
    checks+=3
    print(f"PASS: {checks} exact rational assertions")
if __name__=="__main__": main()
