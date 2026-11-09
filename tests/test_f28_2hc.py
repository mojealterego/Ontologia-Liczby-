from fractions import Fraction as Q
from itertools import product

def vertices(a, rho):
    r=len(a); lo=[-min(rho,x) for x in a]; out=set()
    for free in range(r):
        fixed=[j for j in range(r) if j!=free]
        for bits in product((0,1),repeat=r-1):
            u=[Q(0)]*r
            for j,b in zip(fixed,bits): u[j]=rho if b else lo[j]
            u[free]=-sum(u)
            if lo[free]<=u[free]<=rho: out.add(tuple(u))
    return out

def test():
    count=0
    for r in (2,3):
      for a in product((Q(1,2),Q(1),Q(2)),repeat=r):
       for rho in (Q(0),Q(1,4),Q(1,2),Q(1),Q(2)):
        vs=vertices(a,rho)
        assert vs
        for d in product((Q(-1),Q(0),Q(2)),repeat=r):
         exact=min(sum(x*y for x,y in zip(d,u)) for u in vs)
         for t in product((Q(-2),Q(-1),Q(0),Q(1),Q(2)),repeat=r-1):
          u=tuple(rho*x/2 for x in t); u=u+(-sum(u),)
          if all(-min(rho,x)<=v<=rho for x,v in zip(a,u)):
           assert sum(x*y for x,y in zip(d,u))>=exact
         count+=1
    assert count==4050,count
    print('PASS',count,'exact vertex/grid comparisons')
if __name__=='__main__': test()
