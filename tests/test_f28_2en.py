from fractions import Fraction as F
from itertools import product

def blocks(labels):
    return [set(i for i,x in enumerate(labels) if x==a) for a in sorted(set(labels))]
def join(p,q,n):
    parent=list(range(n))
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    for partition in (p,q):
        for b in partition:
            for a in b:parent[root(a)]=root(next(iter(b)))
    return blocks([root(i) for i in range(n)])
def meet(p,q):
    return [a&b for a in p for b in q if a&b]
def cost(p,x,w):
    s=F(0)
    for b in p:
        z=sum((w[i]*x[i] for i in b),F(0))/sum((w[i] for i in b),F(0))
        s+=sum((w[i]*(x[i]-z)**2 for i in b),F(0))
    return s
def check():
    checks=0
    for n in range(2,5):
        for lp in product(range(n),repeat=n):
            p=blocks(lp)
            for lq in product(range(n),repeat=n):
                q=blocks(lq)
                j=join(p,q,n);m=meet(p,q)
                assert len(m)+len(j)>=len(p)+len(q)
                checks+=1
                for v in product((-1,0,2),repeat=n):
                    x=list(map(F,v));w=[F(i+1) for i in range(n)]
                    h=[F(next(iter(sorted(b)))+1) for i in range(n) for b in []] # overwritten below
                    h=[F(next(k+1 for k,b in enumerate(j) if i in b)) for i in range(n)]
                    assert cost(p,[x[i]+h[i] for i in range(n)],w)==cost(p,x,w)
                    assert cost(q,[x[i]+h[i] for i in range(n)],w)==cost(q,x,w)
                    checks+=2
    print("PASS",checks,"exact checks")
if __name__=="__main__":check()
