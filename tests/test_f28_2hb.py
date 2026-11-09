from fractions import Fraction as Q
from itertools import product
def allocations(r,N):
    return [p for p in product(range(1,N+1),repeat=r) if sum(p)==N]
def h(a,n,m,rho):
    d=[Q(1,x**5)-Q(1,y**5) for x,y in zip(m,n)]
    gap=sum(x*y for x,y in zip(a,d))
    return gap-rho*sum(-x for x in d if x<0)-sum(x*min(rho,w) for x,w in zip(d,a) if x>0)
def test():
    checks=0
    for r in (2,3):
      for N in range(r+1,r+4):
       for a0 in product((1,2,3),repeat=r):
        a=tuple(map(Q,a0)); A=allocations(r,N)
        v=lambda n:sum(w/Q(x**5) for w,x in zip(a,n))
        best=min(map(v,A)); opts=[n for n in A if v(n)==best]
        if len(opts)!=1:continue
        n=opts[0]
        for m in A:
         if m==n:continue
         for rho in (Q(0),Q(1,2),Q(1),Q(2),Q(4)):
          d=[Q(1,x**5)-Q(1,y**5) for x,y in zip(m,n)]
          expected=sum(min((w+e)*z for e in (-min(rho,w),rho)) for w,z in zip(a,d))
          assert h(a,n,m,rho)==expected
          checks+=1
    print('PASS',checks,'exact rational comparisons')
if __name__=='__main__':test()
