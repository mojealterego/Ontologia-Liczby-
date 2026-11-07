from fractions import Fraction as F
from itertools import product

def run():
    checks=0
    for x in product((-2,0,3), repeat=3):
        for weights in product((1,2), repeat=3):
            w=list(map(F,weights)); xx=list(map(F,x))
            mean=sum(a*b for a,b in zip(w,xx))/sum(w)
            q=[mean]*3
            residual=[a-b for a,b in zip(xx,q)]
            for params in ((F(1,2),F(3,2),F(1,3)),(F(0),F(2),F(3)),(F(1),F(3,2),F(1,2))):
                state=xx[:]; p=F(1); r0=sum(a*b*b for a,b in zip(w,residual))
                for alpha in params:
                    before=sum(wi*(si-qi)**2 for wi,si,qi in zip(w,state,q))
                    after=[si+alpha*(qi-si) for si,qi in zip(state,q)]
                    after_r=sum(wi*(si-qi)**2 for wi,si,qi in zip(w,after,q))
                    assert before==p*p*r0; checks+=1
                    assert before-after_r==alpha*(2-alpha)*before; checks+=1
                    assert sum(wi*si for wi,si in zip(w,after))==sum(wi*si for wi,si in zip(w,xx)); checks+=1
                    if alpha:
                        delta=sum(wi*(a-b)**2 for wi,a,b in zip(w,state,after))
                        assert delta==alpha*alpha*before; checks+=1
                    state=after; p*=1-alpha
                assert state==[qi+p*ri for qi,ri in zip(q,residual)]; checks+=1
    print(f"PASS {checks} exact rational assertions")
if __name__=="__main__":
    run()
