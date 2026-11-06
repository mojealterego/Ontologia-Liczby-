from fractions import Fraction as F
from itertools import product

def H(x,w,blocks):
    W=sum(w)
    mu=sum(a*b for a,b in zip(x,w))/W
    return sum(sum(w[i] for i in B)*(sum(w[i]*x[i] for i in B)/sum(w[i] for i in B)-mu)**2 for B in blocks)

def K(x,h,w,blocks):
    W=sum(w)
    mx=sum(a*b for a,b in zip(x,w))/W
    mh=sum(a*b for a,b in zip(h,w))/W
    return sum(sum(w[i] for i in B)*(sum(w[i]*x[i] for i in B)/sum(w[i] for i in B)-mx)*(sum(w[i]*h[i] for i in B)/sum(w[i] for i in B)-mh) for B in blocks)

def partitions(n):
    def rec(i,bs):
        if i==n:
            yield [tuple(B) for B in bs]
        else:
            for j in range(len(bs)):
                bs[j].append(i)
                yield from rec(i+1,bs)
                bs[j].pop()
            bs.append([i])
            yield from rec(i+1,bs)
            bs.pop()
    yield from rec(0,[])

def test_exact():
    count=0
    for n in (2,3):
        for weights in product((1,2),repeat=n):
            w=tuple(map(F,weights))
            for x0 in product((-1,0,2),repeat=n):
                x=tuple(map(F,x0))
                for h0 in product((-1,0,1),repeat=n):
                    h=tuple(map(F,h0))
                    for P in partitions(n):
                        a=H(x,w,P); b=H(h,w,P); k=K(x,h,w,P)
                        assert H(tuple(x[i]+h[i] for i in range(n)),w,P)==a+2*k+b
                        assert k*k<=a*b
                        assert b<=sum(w)
                        if b==0:
                            assert H(tuple(x[i]+h[i] for i in range(n)),w,P)==a
                        count+=4
    print(f"PASS {count} exact rational assertions")

if __name__=="__main__":
    test_exact()
