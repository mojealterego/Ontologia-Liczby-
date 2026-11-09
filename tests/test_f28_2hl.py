from fractions import Fraction as F
from itertools import product

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def margin(vertices, costs, index=0):
    x=vertices[index]
    gaps=[]
    for j,v in enumerate(vertices):
        if j==index: continue
        d=tuple(v[k]-x[k] for k in range(len(x)))
        gaps.append(dot(costs,d)/sum(map(abs,d)))
    return min(gaps) if gaps else None

def verify():
    checks=0
    triangle=((F(0),F(0)),(F(1),F(0)),(F(0),F(1)))
    for a,b in product(range(1,12),repeat=2):
        c=(F(a),F(b))
        mu=margin(triangle,c)
        assert mu==min(c)
        for e1,e2 in product(range(-10,11),repeat=2):
            e=(F(e1,12),F(e2,12))
            if max(abs(e1),abs(e2))/12 < mu:
                assert all(dot(tuple(c[k]+e[k] for k in range(2)),v)>0 for v in triangle[1:])
            checks+=1
    assert margin(((F(0),),(F(1),)),(F(0),))==0
    assert margin(((F(0),),(F(1),)),(F(3),))==3
    assert margin(((F(0),F(1)),(F(1),F(0))),(F(3),F(1)))==1
    return checks

if __name__=="__main__":
    print("PASS",verify(),"exact rational perturbation checks")
