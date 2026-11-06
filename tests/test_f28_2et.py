from fractions import Fraction as F
from itertools import product

def energy(xs):
    w=sum(v for x,v in xs)
    m=sum(x*v for x,v in xs)
    q=sum(x*x*v for x,v in xs)
    return q-m*m/w

checks=0
for n,m in product(range(1,3),repeat=2):
    for vals in product(range(-1,3),repeat=n+m):
        for weights in product((1,2),repeat=n+m):
            A=list(zip(map(F,vals[:n]),map(F,weights[:n])))
            B=list(zip(map(F,vals[n:]),map(F,weights[n:])))
            for i in range(n):
                for j in range(m):
                    if A[i][1]!=B[j][1]:
                        continue
                    p,v=A[i]
                    q,_=B[j]
                    wa=sum(z[1] for z in A)
                    wb=sum(z[1] for z in B)
                    ma=sum(x*w for x,w in A)/wa
                    mb=sum(x*w for x,w in B)/wb
                    AA=A.copy()
                    BB=B.copy()
                    AA[i],BB[j]=BB[j],AA[i]
                    delta=energy(AA)+energy(BB)-energy(A)-energy(B)
                    predicted=2*v*(q-p)*(mb-ma)-v*v*(q-p)**2*(1/wa+1/wb)
                    assert delta==predicted,(A,B,i,j,delta,predicted)
                    checks+=1
print('PASS',checks,'exact rational comparisons')
