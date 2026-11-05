from fractions import Fraction as F
from itertools import combinations_with_replacement

def energy(q, cuts):
    n=len(q); out=F(0)
    for a,b in zip(cuts,cuts[1:]):
        xs=q[a:b]; m=sum(xs,F(0))/len(xs)
        out+=sum(((x-m)**2 for x in xs),F(0))/n
    return out

def gain(q,k):
    n=len(q); a=q[:k]; b=q[k:]
    ml=sum(a,F(0))/len(a); mr=sum(b,F(0))/len(b)
    return F(k*(n-k),n*n)*(ml-mr)**2

def test_exact_split():
    count=0
    for q in combinations_with_replacement(range(4),6):
        for k in range(1,6):
            assert energy(q,[0,6])-energy(q,[0,k,6])==gain(q,k)
            count+=1
    assert count==420

def test_certificate():
    for q in combinations_with_replacement(range(4),6):
        e=energy(q,[0,6])
        u=F((q[-1]-q[0])**2,4)
        assert e<=u

def test_linear():
    q=[F(i,6) for i in range(6)]
    assert energy(q,[0,6])==F(35,432)
