from fractions import Fraction as F
from itertools import product

def q(x, blocks, w):
    y = list(x)
    for b in blocks:
        m = sum((w[i]*x[i] for i in b), F(0)) / sum((w[i] for i in b), F(0))
        for i in b:
            y[i] = m
    return tuple(y)

P=((0,1),(2,)); R=((0,),(1,2)); w=(F(1),)*3
T=lambda x:q(q(x,P,w),R,w)
checks=0
for x in product((-1,0,1),repeat=3):
    x=tuple(map(F,x)); z=q(x,P,w); u=T(x)
    norm=lambda v:sum((a*a for a in v),F(0))
    sub=lambda a,b:tuple(i-j for i,j in zip(a,b))
    assert norm(x)-norm(u)==norm(sub(x,z))+norm(sub(z,u))
    checks+=1

y=(F(1),F(0),F(-1)); t=T(y)
assert t==(F(1,2),F(-1,4),F(-1,4));checks+=1
assert T(t)==tuple(v/F(4) for v in t);checks+=1
for k in range(1,10):
    a=y
    for _ in range(k):a=T(a)
    assert a==tuple(v/F(4)**(k-1) for v in t);checks+=1

P4=((0,1),(2,3));R4=((0,2),(1,3));w4=(F(1),)*4
for x in product((0,1,2),repeat=4):
    x=tuple(map(F,x))
    a=q(q(x,P4,w4),R4,w4)
    b=q(q(x,R4,w4),P4,w4)
    assert a==b==(sum(x)/4,)*4
    checks+=1
print("PASS",checks,"exact rational assertions")
