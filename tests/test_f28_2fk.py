from fractions import Fraction as F
from itertools import product
def Q(x,w):
    s=sum((a*b for a,b in zip(x,w)),F(0))/sum(w)
    return tuple(s for _ in x)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def mul(a,x): return tuple(a*t for t in x)
def sub(x,y): return add(x,mul(-1,y))
checks=0
for w in product((F(1),F(2)),repeat=2):
 for x in product((F(-1),F(0),F(2)),repeat=2):
  for e in product((F(-1),F(0),F(1)),repeat=2):
   for a in (F(-1,2),F(0),F(1,3),F(1,2)):
    z=x; qx=Q(x,w); px=sub(x,qx); qe=Q(e,w); pe=sub(e,qe)
    for k in range(1,6):
     z=add(add(Q(z,w),mul(a,sub(z,Q(z,w)))),e)
     expected=add(add(qx,mul(k,qe)),add(mul(a**k,px),mul(sum((a**j for j in range(k)),F(0)),pe)))
     assert z==expected,(w,x,e,a,k,z,expected)
     checks+=1
print("PASS",checks,"exact rational identities")
