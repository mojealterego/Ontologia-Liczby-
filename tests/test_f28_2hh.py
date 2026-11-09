from fractions import Fraction as F
from itertools import product

def value(d,s):
    feasible=[(F(k,4),s-F(k,4)) for k in range(5) if 0<=s-F(k,4)<=1]
    return min(sum(a*b for a,b in zip(d,u)) for u in feasible)

def test():
    count=0
    for s in (F(k,4) for k in range(9)):
        feasible=[(F(k,4),s-F(k,4)) for k in range(5) if 0<=s-F(k,4)<=1]
        for d0,d1,e0,e1 in product(range(-2,3),repeat=4):
            d=(F(d0),F(d1));e=(F(e0),F(e1))
            old=value(d,s)
            new=value(tuple(d[i]+e[i] for i in range(2)),s)
            alpha=max(abs(sum(e[i]*u[i] for i in range(2))) for u in feasible)
            assert abs(new-old)<=alpha
            for u in feasible:
                if sum(d[i]*u[i] for i in range(2))==old:
                    regret=sum((d[i]+e[i])*u[i] for i in range(2))-new
                    diameter=max(sum(abs(u[i]-v[i]) for i in range(2)) for v in feasible)
                    assert 0<=regret<=max(abs(x) for x in e)*diameter
            assert value(tuple(d[i]+3 for i in range(2)),s)==old+3*s
            count+=1
    return count

if __name__=="__main__":
    print("PASS",test(),"exact rational instances")
