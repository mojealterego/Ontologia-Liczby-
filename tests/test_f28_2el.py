from fractions import Fraction as F
from itertools import product

def cost(z, blocks, w):
    result=F(0)
    for b in blocks:
        mass=sum((w[i] for i in b),F(0))
        mean=sum((w[i]*z[i] for i in b),F(0))/mass
        result+=sum((w[i]*(z[i]-mean)**2 for i in b),F(0))
    return result

def partitions(n):
    for mask in range(1<<(n-1)):
        blocks=[]; start=0
        for i in range(n-1):
            if mask>>i&1:
                blocks.append(tuple(range(start,i+1))); start=i+1
        blocks.append(tuple(range(start,n)))
        yield tuple(blocks)

def test_quadratic_identity():
    checks=0
    for n in range(2,5):
        for vals in product(range(-1,2),repeat=n):
            for direction in product(range(-1,2),repeat=n):
                x=list(map(F,vals)); h=list(map(F,direction))
                w=[F(i+1) for i in range(n)]
                for p in partitions(n):
                    c=cost(x,p,w)
                    plus=cost([x[i]+h[i] for i in range(n)],p,w)
                    minus=cost([x[i]-h[i] for i in range(n)],p,w)
                    a=(plus+minus)/2-c
                    b=(plus-minus)/4
                    assert a>=0
                    for t in (F(-2),F(-1,2),F(0),F(1,3),F(2)):
                        assert cost([x[i]+t*h[i] for i in range(n)],p,w)==c+2*b*t+a*t*t
                        checks+=1
    assert checks==277830

if __name__=="__main__":
    test_quadratic_identity()
    print("PASS 277830 exact rational identities")
