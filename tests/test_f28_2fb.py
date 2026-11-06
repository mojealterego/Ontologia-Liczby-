from fractions import Fraction as F
from itertools import product
def partitions(n):
    if n==0: yield (); return
    for p in partitions(n-1):
        yield p+((n-1,),)
        for k in range(len(p)):
            yield p[:k]+(p[k]+(n-1,),)+p[k+1:]
def proj(x,w,p):
    y=list(x)
    for b in p:
        m=sum((w[i]*x[i] for i in b),F(0))/sum((w[i] for i in b),F(0))
        for i in b:y[i]=m
    return tuple(y)
def diff(x,w,p,r):
    a=proj(proj(x,w,r),w,p);b=proj(proj(x,w,p),w,r)
    return tuple(u-v for u,v in zip(a,b))
def dot(x,y,w):return sum((a*b*c for a,b,c in zip(x,y,w)),F(0))
def main():
    count=0
    for n in (2,3,4):
        ps=list(partitions(n))
        for ww in product((1,2),repeat=n):
            w=tuple(map(F,ww))
            for xx in product((-1,0,2),repeat=n):
                x=tuple(map(F,xx))
                for p in ps:
                    for r in ps:
                        c=diff(x,w,p,r)
                        assert dot(c,x,w)==0
                        assert dot(c,c,w)>=0
                        assert dot(c,c,w)<=4*dot(x,x,w)
                        y=tuple(3*t+7 for t in x)
                        d=diff(y,w,p,r)
                        assert d==tuple(3*t for t in c)
                        count+=4
    p=((0,1),(2,));r=((0,),(1,2));x=(F(1),F(0),F(0));w=(F(1),)*3
    assert dot(diff(x,w,p,r),diff(x,w,p,r),w)==F(1,8)
    print("PASS",count,"exact rational assertions")
if __name__=="__main__":main()
