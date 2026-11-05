from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement

def cost(xs,i,j):
    ys=xs[i:j]
    m=sum(ys,F(0))/len(ys)
    return sum(((x-m)**2 for x in ys),F(0))

def dp(xs,k):
    n=len(xs)
    d=[[None]*(n+1) for _ in range(k+1)]
    d[0][0]=F(0)
    for a in range(1,k+1):
        for j in range(a,n+1):
            d[a][j]=min(d[a-1][t]+cost(xs,t,j) for t in range(a-1,j) if d[a-1][t] is not None)
    return d[k][n]

def brute(xs,k):
    n=len(xs)
    return min(sum((cost(xs,a,b) for a,b in zip((0,)+cuts,cuts+(n,))),F(0)) for cuts in combinations(range(1,n),k-1))

def test_f28_2eb():
    count=0
    for n in range(1,8):
        for tup in combinations_with_replacement(range(4),n):
            xs=list(map(F,tup))
            for k in range(1,n+1):
                assert dp(xs,k)==brute(xs,k)
                count+=1
            assert dp(xs,n)==0
            count+=1
    assert dp(list(map(F,[0,2,4])),2)==2
    assert dp(list(map(F,[0,0,0,10])),2)==0
    assert dp(list(map(F,[0,1,3])),2)==F(1,2)
    return count+3

if __name__=="__main__":
    print("PASS",test_f28_2eb())
