from fractions import Fraction as F
from itertools import product
def dot(x,y,w): return sum((a*b*c for a,b,c in zip(x,y,w)),F(0))
def q(x,w,blocks):
    out=list(x)
    for block in blocks:
        avg=sum((w[i]*x[i] for i in block),F(0))/sum((w[i] for i in block),F(0))
        for i in block: out[i]=avg
    return tuple(out)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(a,t): return tuple(t*x for x in a)
count=0
blocks=((0,1),(2,))
for vals in product((-1,0,2),repeat=3):
 for weights in product((1,2),repeat=3):
  w=tuple(map(F,weights)); x=tuple(map(F,vals)); qx=q(x,w,blocks)
  for ev in product((-1,0,1),repeat=3):
   e=tuple(map(F,ev)); qe=q(e,w,blocks)
   for alpha in (F(1,2),F(1),F(3,2)):
    r=1-alpha; cur=x; tang=(F(0),)*3; trans=sub(x,qx)
    for k in range(4):
     cur=add(add(scale(cur,r),scale(q(cur,w,blocks),alpha)),e)
     tang=add(tang,qe); trans=add(scale(trans,r),sub(e,qe))
     assert q(cur,w,blocks)==add(qx,tang)
     assert sub(cur,q(cur,w,blocks))==trans
     assert dot(sub(cur,qx),sub(cur,qx),w)==dot(tang,tang,w)+dot(trans,trans,w)
     count+=3
print("PASS",count,"exact rational assertions")
