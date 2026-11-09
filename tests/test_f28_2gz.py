from fractions import Fraction as Q
from itertools import product

def d(k):
    return Q(1,k**5)-Q(1,(k+1)**5)

def allocations(r,N):
    for n in product(range(1,N+1),repeat=r):
        if sum(n)==N:
            yield n

def cost(a,n):
    return sum((a[i]/n[i]**5 for i in range(len(a))),Q(0))

def epsilon(a,n):
    if sum(n)==len(n):
        return Q(0)
    L=min(a[i]*d(n[i]-1) for i in range(len(a)) if n[i]>1)
    U=max(a[i]*d(n[i]) for i in range(len(a)))
    return max(Q(0),U-L)

def test_exact_certificate():
    count=0
    for r in (2,3):
        for N in range(r,r+5):
            for aa in product((1,2,3),repeat=r):
                a=tuple(map(Q,aa))
                choices=list(allocations(r,N))
                optimum=min(cost(a,n) for n in choices)
                for n in choices:
                    e=epsilon(a,n)
                    gap=cost(a,n)-optimum
                    assert (e==0)==(gap==0)
                    assert Q(0)<=gap<=(N-r)*e
                    if e==0 and N>r:
                        L=min(a[i]*d(n[i]-1) for i in range(r) if n[i]>1)
                        U=max(a[i]*d(n[i]) for i in range(r))
                        if L>U:
                            assert sum(cost(a,m)==optimum for m in choices)==1
                    count+=1
    assert count==1080

if __name__=="__main__":
    test_exact_certificate()
    print("PASS 1080 exact rational cases")
