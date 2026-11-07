from fractions import Fraction as F
from itertools import product
def proj(x, blocks, w):
    y=list(x)
    for block in blocks:
        m=sum(w[i]*x[i] for i in block)/sum(w[i] for i in block)
        for i in block:y[i]=m
    return tuple(y)
def norm2(x,w):return sum(w[i]*x[i]*x[i] for i in range(len(x)))
P=((0,1),(2,))
R=((0,),(1,2))
checks=0
for ww in product((1,2),repeat=3):
    w=tuple(map(F,ww))
    for xx in product((-1,0,2),repeat=3):
        x=tuple(map(F,xx))
        a=proj(x,P,w);t=proj(a,R,w)
        r=norm2(tuple(x[i]-a[i] for i in range(3)),w)+norm2(tuple(a[i]-t[i] for i in range(3)),w)
        assert r==norm2(x,w)-norm2(t,w)
        checks+=1
        mean=sum(w[i]*x[i] for i in range(3))/sum(w)
        e=(mean,)*3
        assert norm2(tuple(x[i]-e[i] for i in range(3)),w)-norm2(tuple(t[i]-e[i] for i in range(3)),w)==r
        checks+=1
        assert (r==0)==(x==e)
        checks+=1
assert proj(proj((F(1),F(0),F(0)),P,(F(1),)*3),R,(F(1),)*3)==(F(1,2),F(1,4),F(1,4))
print("PASS",checks,"exact rational assertions + example")
