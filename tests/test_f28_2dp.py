from fractions import Fraction as F
from itertools import combinations_with_replacement

def test_exact_quantile_coarsening():
    checks=0
    for n in (2,3,4,5):
        for vals in combinations_with_replacement(range(5),n):
            q=[F(x) for x in vals]
            avg=sum(q,F(0))/n
            error=sum((abs(x-avg) for x in q),F(0))/n
            assert error <= (max(q)-min(q))/2
            checks+=1
    for n in range(1,20):
        h=F(1,n)
        assert n*h*h/4 == F(1,4*n)
        checks+=1
    assert (abs(F(0)-1)+abs(F(2)-1))/2==1
    return checks+1

if __name__=="__main__":
    print("PASS",test_exact_quantile_coarsening(),"exact rational checks")
