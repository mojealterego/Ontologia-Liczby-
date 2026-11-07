from fractions import Fraction as F
from itertools import product

def proj(x,w,parts):
    y=list(x)
    for b in parts:
        m=sum((w[i]*x[i] for i in b),F(0))/sum((w[i] for i in b),F(0))
        for i in b: y[i]=m
    return y

def norm(x,w):
    return sum((w[i]*x[i]*x[i] for i in range(len(x))),F(0))

def sub(x,y):
    return [a-b for a,b in zip(x,y)]

def mix(x,y,a):
    return [(1-a)*u+a*v for u,v in zip(x,y)]

def test_exact_energy():
    P=((0,1),(2,))
    R=((0,),(1,2))
    w=(F(1),F(2),F(3))
    checks=0
    for x0 in product((-2,0,3),repeat=3):
        x=list(map(F,x0))
        for a,b in product((F(1,4),F(1,2),F(1)),repeat=2):
            p=proj(x,w,P)
            u=mix(x,p,a)
            r=proj(u,w,R)
            v=mix(u,r,b)
            lhs=norm(x,w)-norm(v,w)
            rhs=a*(2-a)*norm(sub(x,p),w)+b*(2-b)*norm(sub(u,r),w)
            assert lhs==rhs
            checks+=1
            assert sum(t*z for t,z in zip(w,x))==sum(t*z for t,z in zip(w,v))
            checks+=1
            assert lhs>=0
            checks+=1
            if lhs==0:
                assert x==p and u==r
                checks+=1
    return checks

if __name__=="__main__":
    print("PASS",test_exact_energy(),"exact rational assertions")
