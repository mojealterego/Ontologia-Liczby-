from fractions import Fraction as F
from itertools import product
def dot(x,y,w): return sum((a*b*c for a,b,c in zip(x,y,w)),F(0))
def q(x,w):
 m=sum((a*b for a,b in zip(x,w)),F(0))/sum(w)
 return tuple(m for _ in x)
checks=0
for n in (2,3):
 for ww in product((1,2),repeat=n):
  w=tuple(map(F,ww))
  for xx in product((-1,0,2),repeat=n):
   x=tuple(map(F,xx)); p=q(x,w)
   for alpha in map(F,(-1,0,1,2,3)):
    a=tuple((1-alpha)*v+alpha*u for v,u in zip(x,p))
    e=tuple(v-u for v,u in zip(x,p))
    assert dot(x,x,w)-dot(a,a,w)==alpha*(2-alpha)*dot(e,e,w)
    checks+=1
    assert q(a,w)==p
    checks+=1
    if alpha:
     d=tuple(v-u for v,u in zip(x,a))
     assert dot(d,d,w)==alpha*alpha*dot(e,e,w)
     checks+=1
print('PASS',checks,'exact rational assertions')
