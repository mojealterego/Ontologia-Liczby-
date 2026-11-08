from fractions import Fraction as Q
from itertools import product

def d(k):
    return Q(1,k**5)-Q(1,(k+1)**5)

def allocations(r,N):
    for n in product(range(1,N+1),repeat=r):
        if sum(n)==N:
            yield n

def cost(a,n):
    return sum((x/Q(k**5) for x,k in zip(a,n)),Q(0))

def epsilon(a,n):
    return max([Q(0)]+[a[j]*d(n[j])-a[i]*d(n[i]-1)
        for i in range(len(n)) for j in range(len(n))
        if i!=j and n[i]>1])

def test_f28_2gy():
    count=0
    for r in (2,3):
        for N in range(r,r+5):
            for a in product((Q(1),Q(2),Q(3)),repeat=r):
                choices=list(allocations(r,N))
                best=min(cost(a,m) for m in choices)
                for n in choices:
                    e=epsilon(a,n)
                    gap=cost(a,n)-best
                    assert (e==0)==(gap==0),(a,n,e,gap)
                    assert e<=gap<=(N-r)*e,(a,n,e,gap)
                    count+=1
    assert count==1080

if __name__=="__main__":
    test_f28_2gy()
    print("PASS 1080 exact rational cases")
