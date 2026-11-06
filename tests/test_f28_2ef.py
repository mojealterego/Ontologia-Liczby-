from fractions import Fraction as F
from itertools import combinations, product

def cost(xs,ws,cuts):
    ends=(0,)+tuple(cuts)+(len(xs),)
    ans=F(0)
    for a,b in zip(ends,ends[1:]):
        W=sum(ws[a:b]); m=sum((ws[i]*xs[i] for i in range(a,b)),F(0))/W
        ans+=sum((ws[i]*(xs[i]-m)**2 for i in range(a,b)),F(0))
    return ans

def test_stability():
    count=0
    for n in range(3,6):
        for raw in combinations(range(7),n):
            xs=tuple(map(F,raw)); R=xs[-1]-xs[0]
            for weights in product((1,2),repeat=n):
                ws=tuple(map(F,weights)); W=sum(ws)
                for k in range(2,n):
                    ps=tuple(combinations(range(1,n),k-1))
                    scores={p:cost(xs,ws,p) for p in ps}
                    v=min(scores.values()); opt=[p for p in ps if scores[p]==v]
                    for shift in (F(1,10),F(-1,10)):
                        ys=tuple(x+shift for x in xs)
                        assert all(cost(ys,ws,p)==scores[p] for p in ps);count+=1
                    ys=tuple(2*x+5 for x in xs)
                    assert all(cost(ys,ws,p)==4*scores[p] for p in ps);count+=1
                    delta=F(1,100);ys=tuple(x+delta*(i%2) for i,x in enumerate(xs))
                    assert ys==tuple(sorted(ys))
                    K=4*W*R*delta+4*W*delta**2
                    assert all(abs(cost(ys,ws,p)-scores[p])<=K for p in ps);count+=1
                    assert abs(min(cost(ys,ws,p) for p in ps)-v)<=K;count+=1
                    if len(opt)==1:
                        gamma=min(s-v for p,s in scores.items() if p!=opt[0])
                        if gamma>2*K:
                            assert min(ps,key=lambda p:cost(ys,ws,p))==opt[0];count+=1
    assert cost((F(0),F(1),F(3)),(F(1),)*3,(2,))==F(1,2)
    assert cost((F(0),F(1),F(3)),(F(100),F(1),F(1)),(1,))==F(2)
    assert cost((F(0),F(1),F(3)),(F(100),F(1),F(1)),(2,))==F(100,101)
    print("PASS:",count+3,"exact assertions")

if __name__=="__main__":test_stability()
