"""F28.2-FF: exact rational regression for alternating block averages."""
from fractions import Fraction as F
from itertools import product

def projection(x, weights, partition):
    y = list(x)
    for block in partition:
        m = sum(weights[i]*x[i] for i in block)/sum(weights[i] for i in block)
        for i in block:
            y[i] = m
    return y

def dot(x,y,w):
    return sum(a*b*c for a,b,c in zip(x,y,w))

def check():
    P=((0,1),(2,))
    R=((0,),(1,2))
    checks=0
    for ww in product((1,2,3),repeat=3):
        w=tuple(map(F,ww))
        for values in product((-1,0,2),repeat=3):
            x=list(map(F,values))
            mu=sum(a*b for a,b in zip(w,x))/sum(w)
            e=[mu]*3
            y=x
            residuals=[]
            for k in range(6):
                r=[a-b for a,b in zip(y,e)]
                residuals.append(dot(r,r,w))
                assert sum(a*b for a,b in zip(w,y))==sum(a*b for a,b in zip(w,x))
                checks+=1
                y=projection(projection(y,w,P),w,R)
            for k in range(1,5):
                assert residuals[k+1]<=residuals[k]
                checks+=1
            assert residuals[-1]<=residuals[0]
            checks+=1
    # Explicit unit-weight example: principal-angle cosine 1/2.
    w=(F(1),)*3
    x=[F(1),F(1),F(-2)]
    e=[F(0)]*3
    y=x
    for k in range(1,6):
        y=projection(projection(y,w,P),w,R)
        assert dot(y,y,w)==F(6)*F(1,4)**(2*k-1)
        checks+=1
    return checks

if __name__=="__main__":
    print("PASS",check(),"exact rational checks")
