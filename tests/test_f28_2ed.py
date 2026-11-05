from fractions import Fraction as F
from itertools import combinations_with_replacement

def cost(x,a,b):
    v=x[a:b]
    return sum(t*t for t in v)-sum(v)**2/F(len(v))

def dp(x,k):
    n=len(x); old=[None]*(n+1);old[0]=F(0)
    for layer in range(1,k+1):
        new=[None]*(n+1)
        for j in range(layer,n+1):
            new[j]=min(old[t]+cost(x,t,j) for t in range(layer-1,j) if old[t] is not None)
        old=new
    return old[n]

checks=0
for n in range(2,8):
    for x in combinations_with_replacement(range(4),n):
        x=tuple(map(F,x))
        for a in range(n):
            for b in range(a+1,n+1):
                assert cost(x,a,b)>=0;checks+=1
        for a in range(n):
            for b in range(a,n):
                for c in range(b,n):
                    for d in range(c,n):
                        assert cost(x,a,c+1)+cost(x,b,d+1)<=cost(x,a,d+1)+cost(x,b,c+1);checks+=1
        for k in range(1,min(n,4)+1):
            assert dp(x,k)>=0;checks+=1
y=tuple(map(F,(0,2,0)))
assert cost(y,0,2)+cost(y,1,3)>cost(y,0,3)
print('PASS',checks,'exact rational assertions')
