from fractions import Fraction as F
from itertools import product

def project(x,w,blocks):
    out=list(x)
    for b in blocks:
        avg=sum((w[i]*x[i] for i in b),F(0))/sum((w[i] for i in b),F(0))
        for i in b: out[i]=avg
    return out

def norm(x,w): return sum((wi*xi*xi for wi,xi in zip(w,x)),F(0))
def run():
    P=((0,1),(2,)); R=((0,),(1,2))
    checks=0
    for vals in product((-1,0,2),repeat=3):
      for weights in product((1,2),repeat=3):
        x=list(map(F,vals));w=list(map(F,weights))
        y=project(x,w,P);z=project(y,w,R)
        assert norm(x,w)-norm(z,w)==norm([a-b for a,b in zip(x,y)],w)+norm([a-b for a,b in zip(y,z)],w)
        checks+=1
        assert sum((a*b for a,b in zip(x,w)),F(0))==sum((a*b for a,b in zip(z,w)),F(0))
        checks+=1
        cur=x
        for _ in range(160): cur=project(project(cur,w,P),w,R)
        avg=sum((a*b for a,b in zip(x,w)),F(0))/sum(w)
        assert max(abs(a-avg) for a in cur)<F(1,10**10)
        checks+=1
    assert project(project([F(0),F(2),F(4)],[F(1)]*3,P),[F(1)]*3,R)==[F(1),F(5,2),F(5,2)]
    return checks+1
if __name__=="__main__": print("PASS",run())
