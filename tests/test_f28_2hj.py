"""Exact rational regression for F28.2-HJ."""
from fractions import Fraction as Q
from itertools import product

def quotient_inf(e):
    return (max(e)-min(e))/2

def value(c, vertices):
    return min(sum(a*b for a,b in zip(c,u)) for u in vertices)

def test_segment():
    vertices = [(Q(0),Q(1)), (Q(1),Q(0))]
    u0 = (Q(1,2),Q(1,2))
    L = max(sum(abs(x-y) for x,y in zip(u,u0)) for u in vertices)
    assert L == 1
    count = 0
    for c in product(range(-4,5),repeat=2):
        for e in product(range(-3,4),repeat=2):
            c = tuple(map(Q,c)); e = tuple(map(Q,e))
            W = lambda z: value(z,vertices)-sum(x*y for x,y in zip(z,u0))
            shifted = tuple(x+y for x,y in zip(c,e))
            assert abs(W(shifted)-W(c)) <= L*quotient_inf(e)
            assert W(tuple(x+Q(7) for x in c)) == W(c)
            count += 1
    assert count == 3969
    return count

if __name__ == "__main__":
    print("PASS",test_segment(),"exact rational instances")
