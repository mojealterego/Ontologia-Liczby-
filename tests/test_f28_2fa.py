from fractions import Fraction as F
from itertools import product

def partitions(n):
    def rec(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from rec(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from rec(i + 1, blocks)
        blocks.pop()
    yield from rec(0, [])

def dot(a,b,w):
    return sum((wi*ai*bi for wi,ai,bi in zip(w,a,b)), F(0))

def project(x,w,p):
    y=list(x)
    for block in p:
        mean=sum((w[i]*x[i] for i in block),F(0))/sum((w[i] for i in block),F(0))
        for i in block: y[i]=mean
    return y

def h(x,w,p):
    e=project(x,w,p)
    mu=sum((a*b for a,b in zip(w,x)),F(0))/sum(w)
    return dot([a-mu for a in e],[a-mu for a in e],w)

def d(x,w,p,r):
    a,b=project(x,w,p),project(x,w,r)
    return dot([u-v for u,v in zip(a,b)],[u-v for u,v in zip(a,b)],w)

def join(p,r):
    return tuple(tuple(sorted(set(a)&set(b))) for a in p for b in r if set(a)&set(b))

checks=0
for n in (2,3,4):
    ps=list(partitions(n))
    for vals in product((0,1,2),repeat=n):
        x=tuple(map(F,vals))
        for weights in product((1,2),repeat=n):
            w=tuple(map(F,weights))
            for p in ps:
                hp=h(x,w,p)
                for r in ps:
                    hr=h(x,w,r)
                    delta=d(x,w,p,r)
                    ep,er=project(x,w,p),project(x,w,r)
                    mu=sum((a*b for a,b in zip(w,x)),F(0))/sum(w)
                    cross=dot([a-mu for a in ep],[b-mu for b in er],w)
                    assert delta==hp+hr-2*cross
                    j=join(p,r)
                    assert 0<=delta<=2*(2*h(x,w,j)-hp-hr)
                    assert (delta==0)==(ep==er)
                    checks+=3
assert d(tuple(map(F,(1,0,0,0))),tuple(map(F,(1,1,1,1))),((0,1),(2,3)),((0,2),(1,3)))==F(1,2)
print("PASS",checks,"exact rational assertions")
