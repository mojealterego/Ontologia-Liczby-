from fractions import Fraction as F
from itertools import product

def H_atom(values, weights, t):
    assert sum(weights)==1 and 0<=t<=1
    left=F(1)-t
    total=F(0); u=F(0)
    for x,w in zip(values,weights):
        end=u+w
        total+=x*max(F(0),end-max(u,left))
        u=end
    return total

checks=0
for n in range(1,5):
    for ws in product(range(1,5),repeat=n):
        w=[F(x,sum(ws)) for x in ws]
        vals=list(map(F,range(n)))
        for k in range(0,11):
            t=F(k,10)
            h=H_atom(vals,w,t)
            assert h>=0
            if k>0:
                left=H_atom(vals,w,F(k-1,10))
                assert h>=left
            if k>1:
                prev=H_atom(vals,w,F(k-1,10))
                prevprev=H_atom(vals,w,F(k-2,10))
                assert h-prev<=prev-prevprev
            checks+=1
        for i,x in enumerate(vals):
            upper=sum(w[i+1:]); lower=upper+w[i]
            slope=(H_atom(vals,w,lower)-H_atom(vals,w,upper))/w[i]
            assert slope==x
            checks+=1
print('PASS',checks,'exact rational checks')
