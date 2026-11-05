from fractions import Fraction as F
from itertools import combinations_with_replacement

def energy(q, cuts):
    total=F(0)
    for a,b in zip(cuts,cuts[1:]):
        xs=q[a:b]; m=sum(xs,F(0))/len(xs)
        total+=sum(((x-m)**2 for x in xs),F(0))/len(q)
    return total

def gain(q,a,c,b):
    l=q[a:c]; r=q[c:b]
    ml=sum(l,F(0))/len(l); mr=sum(r,F(0))/len(r)
    return F(len(l)*len(r),len(q)*(len(l)+len(r)))*(ml-mr)**2

def test_exact_gain():
    for n in range(3,8):
        for tup in combinations_with_replacement(range(4),n):
            q=[F(x) for x in tup]
            for c in range(1,n):
                g=gain(q,0,c,n)
                assert energy(q,[0,n])-energy(q,[0,c,n])==g
                assert F(0)<=g<=energy(q,[0,n])

def test_greedy_counterexample():
    q=list(map(F,(0,0,1,2,4))); n=len(q)
    first=max(range(1,n),key=lambda c:gain(q,0,c,n))
    assert first==3
    greedy=min(energy(q,sorted([0,first,c,n])) for c in range(1,n) if c!=first)
    optimum=min(energy(q,[0,a,b,n]) for a in range(1,n) for b in range(a+1,n))
    assert greedy==F(2,15) and optimum==F(1,10)
