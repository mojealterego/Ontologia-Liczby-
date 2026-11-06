from fractions import Fraction as F
from itertools import product

def energy(x,w,blocks):
    W=sum(w); M=sum(a*b for a,b in zip(x,w)); mu=M/W
    return sum(sum(w[i] for i in B)*(sum(w[i]*x[i] for i in B)/sum(w[i] for i in B)-mu)**2 for B in blocks)

checks=0
for n in (2,3,4):
    for x0 in product((-2,0,3),repeat=n):
        x=tuple(map(F,x0))
        for w0 in product((1,2),repeat=n):
            w=tuple(map(F,w0)); W=sum(w)
            for labels in product(range(2),repeat=n):
                if 0 not in labels or 1 not in labels: continue
                blocks=[tuple(i for i in range(n) if labels[i]==j) for j in (0,1)]
                H=energy(x,w,blocks)
                for k in range(n):
                    B=blocks[labels[k]]; WB=sum(w[i] for i in B)
                    muB=sum(w[i]*x[i] for i in B)/WB
                    mu=sum(w[i]*x[i] for i in range(n))/W
                    c=w[k]**2*(1/WB-1/W)
                    assert c>0
                    for t in map(F,(-3,-1,0,1,4)):
                        y=list(x); y[k]+=t
                        assert energy(y,w,blocks)-H==2*w[k]*t*(muB-mu)+c*t*t
                        checks+=1
print('PASS',checks,'exact rational perturbation identities')
