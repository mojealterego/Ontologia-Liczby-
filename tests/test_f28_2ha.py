from fractions import Fraction as Q
from itertools import product
def allocations(r,N):
    return [n for n in product(range(1,N+1),repeat=r) if sum(n)==N]
def value(a,n):
    return sum((x/Q(k**5) for x,k in zip(a,n)),Q(0))
def radius(a,n,opts):
    gaps=[((value(a,m)-value(a,n)),sum((abs(Q(1,k**5)-Q(1,j**5)) for k,j in zip(m,n)),Q(0))) for m in opts if m!=n]
    return min((g/l for g,l in gaps),default=None)
def test_exact_radius():
    count=0
    for r in (2,3):
      for N in range(r+1,r+5):
       opts=allocations(r,N)
       for a0 in product((1,2,3),repeat=r):
        a=tuple(map(Q,a0)); n=min(opts,key=lambda x:value(a,x))
        R=radius(a,n,opts)
        assert R is not None and R>=0
        for h0 in product((-1,0,1),repeat=r):
         h=tuple(R*Q(v,2) for v in h0)
         assert value(tuple(x+y for x,y in zip(a,h)),n)<=min(value(tuple(x+y for x,y in zip(a,h)),m) for m in opts)
         count+=1
    return count
if __name__=="__main__":
 print("PASS",test_exact_radius())
