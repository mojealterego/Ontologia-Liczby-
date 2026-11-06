from fractions import Fraction as F
from itertools import product

def state(items):
    W=sum((w for x,w in items),F(0))
    if not W: return W,None,F(0)
    mu=sum((w*x for x,w in items),F(0))/W
    return W,mu,sum((w*(x-mu)**2 for x,w in items),F(0))

def check():
    count=0
    for n in range(1,5):
        for xs in product((F(-2),F(0),F(3)),repeat=n):
            for ws in product((F(1),F(2)),repeat=n):
                items=list(zip(xs,ws))
                W,mu,S=state(items)
                for z in (F(-1),F(2)):
                    for v in (F(1),F(3)):
                        W2,mu2,S2=state(items+[(z,v)])
                        assert W2==W+v
                        assert mu2==mu+v*(z-mu)/(W+v)
                        assert S2==S+W*v*(z-mu)**2/(W+v)
                        assert S2-W2*v*(z-mu2)**2/W==S
                        count+=4
                if n>1:
                    for i,(z,v) in enumerate(items):
                        Wr,mur,Sr=state(items[:i]+items[i+1:])
                        assert mur==(W*mu-v*z)/(W-v)
                        assert Sr==S-W*v*(z-mu)**2/(W-v)
                        count+=2
    return count

if __name__=="__main__":
    print("PASS exact rational assertions:",check())
