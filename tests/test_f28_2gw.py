"""Exact rational regression for F28.2-GW. Run: python tests/test_f28_2gw.py"""
from fractions import Fraction as Q
from itertools import product

def allocations(r, N):
    return [n for n in product(range(1, N+1), repeat=r) if sum(n)==N]

def verify():
    cases=0
    for r in (2,3):
        for N in range(r,r+5):
            for a in product((Q(1),Q(2),Q(3)),repeat=r):
                ns=allocations(r,N)
                B={}
                for n in ns:
                    s=n[0]-1
                    v=sum(a[j]/n[j]**5 for j in range(1,r))
                    B[s]=min(B.get(s,v),v)
                for t in (Q(-1,2),Q(0),Q(1,3),Q(1),Q(3)):
                    if a[0]+t<=0:continue
                    costs={n:sum((a[j]+(t if j==0 else 0))/n[j]**5 for j in range(r)) for n in ns}
                    optimum=min(costs.values())
                    lines={s:b+(a[0]+t)/Q((s+1)**5) for s,b in B.items()}
                    assert optimum==min(lines.values())
                    active={s for s,v in lines.items() if v==optimum}
                    assert active=={n[0]-1 for n,v in costs.items() if v==optimum}
                    for s in B:
                        cert=all((Q(1,(s+1)**5)-Q(1,(u+1)**5))*(t-((B[u]-B[s])/(Q(1,(s+1)**5)-Q(1,(u+1)**5))-a[0]))<=0 for u in B if u!=s)
                        assert cert==(s in active)
                    cases+=1
    assert cases==900
    assert Q(1,16)<1+Q(1,243)
    print("PASS",cases,"exact rational cases")

if __name__=="__main__":verify()
