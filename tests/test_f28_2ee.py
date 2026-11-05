from fractions import Fraction as F
from itertools import combinations, product

def cost(xs, ws, a, b):
    W=sum(ws[a:b],F(0)); S=sum((ws[i]*xs[i] for i in range(a,b)),F(0))
    Q=sum((ws[i]*xs[i]*xs[i] for i in range(a,b)),F(0))
    return Q-S*S/W

def reference(xs,ws,k):
    n=len(xs); dp=[[None]*(n+1) for _ in range(k+1)]; cut=[[None]*(n+1) for _ in range(k+1)]
    dp[0][0]=F(0)
    for r in range(1,k+1):
        for j in range(r,n+1):
            val,t=min((dp[r-1][t]+cost(xs,ws,t,j),t) for t in range(r-1,j) if dp[r-1][t] is not None)
            dp[r][j]=val;cut[r][j]=t
    j=n; bounds=[n]
    for r in range(k,0,-1):
        j=cut[r][j];bounds.append(j)
    return dp[k][n],tuple(reversed(bounds))

def divide_conquer(xs,ws,k):
    n=len(xs);prev=[None]*(n+1);prev[0]=F(0); rows=[]
    for r in range(1,k+1):
        curr=[None]*(n+1); opt=[None]*(n+1)
        def solve(left,right,lo,hi):
            if left>right:return
            mid=(left+right)//2
            choices=((prev[t]+cost(xs,ws,t,mid),t) for t in range(max(r-1,lo),min(mid-1,hi)+1) if prev[t] is not None)
            best,t=min(choices)
            curr[mid]=best;opt[mid]=t
            solve(left,mid-1,lo,t);solve(mid+1,right,t,hi)
        solve(r,n,r-1,n-1)
        prev=curr;rows.append(opt)
    j=n;bounds=[n]
    for r in range(k,0,-1):
        j=rows[r-1][j];bounds.append(j)
    return prev[n],tuple(reversed(bounds))

def run():
    checks=0
    for n in range(1,7):
        for xs0 in combinations(range(8),n):
            xs=tuple(map(F,xs0))
            for ws0 in product((1,2),repeat=n):
                ws=tuple(map(F,ws0))
                for k in range(1,n+1):
                    a=reference(xs,ws,k);b=divide_conquer(xs,ws,k)
                    assert a==b,(xs,ws,k,a,b)
                    assert len(b[1])==k+1 and b[1][0]==0 and b[1][-1]==n
                    assert sum((cost(xs,ws,b[1][i],b[1][i+1]) for i in range(k)),F(0))==b[0]
                    checks+=3
    print('PASS',checks,'assertions')
if __name__=='__main__':run()
