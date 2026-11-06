from fractions import Fraction as F
from itertools import product
def stats(xs,ws):
 W=sum(ws); M=sum((w*x for w,x in zip(ws,xs)),F(0))
 S=sum((w*x*x for w,x in zip(ws,xs)),F(0))-M*M/W
 D=sum((ws[i]*ws[j]*(xs[i]-xs[j])**2 for i in range(len(xs)) for j in range(i+1,len(xs))),F(0))
 assert S==D/W
 return W,M,S
count=0
for n in range(2,5):
 for xs0 in product(range(-1,3),repeat=n):
  xs=tuple(map(F,xs0))
  for ws0 in product((1,2),repeat=n):
   ws=tuple(map(F,ws0))
   W,M,S=stats(xs,ws);count+=1
   for k in range(1,n):
    a,b=stats(xs[:k],ws[:k]),stats(xs[k:],ws[k:])
    c=a[0]*b[0]/(a[0]+b[0])*(a[1]/a[0]-b[1]/b[0])**2
    assert S==a[2]+b[2]+c and c>=0
    count+=1
   yy=tuple(3*x+5 for x in xs)
   assert stats(yy,ws)[2]==9*S
   count+=1
print('PASS',count,'exact rational checks')
