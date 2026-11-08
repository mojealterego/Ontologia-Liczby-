from fractions import Fraction as Q
from itertools import product

def allocations(r,N):
    return [x for x in product(range(1,N+1),repeat=r) if sum(x)==N]

def profiles(a,N,i):
    r=len(a); A=allocations(r,N)
    return {k:min(sum(a[j]/Q(n[j]**5) for j in range(r) if j!=i) for n in A if n[i]==k) for k in range(1,N-r+2)}

def check():
    cases=0
    for r in (2,3):
      for N in range(r+1,r+5):
       for weights in product((Q(1),Q(2),Q(3)),repeat=r):
        a=list(weights);i=0;B=profiles(a,N,i); A=allocations(r,N)
        prev=None
        for t in map(Q,range(0,13)):
         costs=[sum((a[j]+(t if j==i else 0))/Q(n[j]**5) for j in range(r)) for n in A]
         vals={k:B[k]+(a[i]+t)/Q(k**5) for k in B}
         assert min(costs)==min(vals.values())
         active=[k for k,v in vals.items() if v==min(vals.values())]
         if prev is not None: assert min(active)>=min(prev)
         prev=active
         cases+=1
    return cases

if __name__=='__main__': print('PASS',check())
