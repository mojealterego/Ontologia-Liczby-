from fractions import Fraction as F
from itertools import combinations, product

def cost(z,blocks):
    s=F(0)
    for a,b in blocks:
        v=z[a:b]; m=sum(v,F(0))/len(v)
        s+=sum(((q-m)**2 for q in v),F(0))
    return s

def parts(n,k):
    for cuts in combinations(range(1,n),k-1):
        e=(0,)+cuts+(n,)
        yield tuple(zip(e,e[1:]))

def order_radius(x,h):
    vals=[(x[i+1]-x[i])/(h[i]-h[i+1]) for i in range(len(x)-1) if h[i]>h[i+1]]
    return min(vals) if vals else None

checks=0
for n in (3,4):
    for x0 in combinations(range(6),n):
        x=tuple(map(F,x0))
        for h0 in product((-1,0,1),repeat=n):
            h=tuple(map(F,h0))
            T=order_radius(x,h)
            for t in (F(0),F(1,4),F(1,2),F(1),F(2),F(4)):
                z=tuple(x[i]+t*h[i] for i in range(n))
                ordered=all(z[i]<=z[i+1] for i in range(n-1))
                assert ordered==(T is None or t<=T)
                checks+=1
            for p in parts(n,2):
                for q in parts(n,2):
                    c=cost(x,q)-cost(x,p)
                    b=(cost(tuple(x[i]+h[i] for i in range(n)),q)-cost(tuple(x[i]+h[i] for i in range(n)),p)-c-(cost(h,q)-cost(h,p)))
                    a=cost(h,q)-cost(h,p)
                    for t in (F(0),F(1,2),F(2)):
                        z=tuple(x[i]+t*h[i] for i in range(n))
                        assert cost(z,q)-cost(z,p)==c+b*t+a*t*t
                        checks+=1
print('PASS',checks,'exact rational assertions')
