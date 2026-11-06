from fractions import Fraction as F
from itertools import combinations, product

def dot(a,b):
    return sum((u*v for u,v in zip(a,b)),F(0))

def residual(x,cuts):
    edges=(0,)+tuple(cuts)+(len(x),)
    out=[]
    for a,b in zip(edges,edges[1:]):
        mean=sum(x[a:b],F(0))/F(b-a)
        out.extend(u-mean for u in x[a:b])
    return out

def cost(x,cuts):
    r=residual(x,cuts)
    return dot(r,r)

def run():
    checks=0
    for n in range(3,5):
        cuts=list(combinations(range(1,n),1))
        for raw in product(range(3),repeat=n):
            x=list(map(F,raw))
            for raw_h in product((-1,0,1),repeat=n):
                h=list(map(F,raw_h))
                y=[a+b for a,b in zip(x,h)]
                for p,q in combinations(cuts,2):
                    rxq=residual(x,q); rxp=residual(x,p)
                    rhq=residual(h,q); rhp=residual(h,p)
                    lhs=cost(y,q)-cost(y,p)
                    rhs=(cost(x,q)-cost(x,p)
                         +2*dot([a-b for a,b in zip(rxq,rxp)],h)
                         +dot(rhq,rhq)-dot(rhp,rhp))
                    assert lhs==rhs
                    checks+=1
    assert cost([F(0),F(1),F(3)],(1,))==2
    assert cost([F(0),F(1),F(3)],(2,))==F(1,2)
    print("PASS",checks+2,"exact assertions")

if __name__=="__main__":
    run()
