from fractions import Fraction as F
from itertools import product

def h_atom(points,t):
    total=F(0);left=t
    for x,p in sorted(points,reverse=True):
        z=min(p,left);total+=x*z;left-=z
        if left==0:break
    return total

def test_bounds():
    cases=0
    for a,b in [(-2,3),(0,1),(0,10)]:
      for x,y in product(range(a,b+1),repeat=2):
       for p in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        m=p*x+(1-p)*y
        for t in [F(0),F(1,5),F(1,4),F(1,2),F(3,4),F(1)]:
         h=h_atom([(x,p),(y,1-p)],t)
         assert t*m<=h<=min(t*b,m-(1-t)*a)
         cases+=1
    assert cases==4830
    assert h_atom([(F(1,2),F(1))],F(1,4))==F(1,8)
    assert h_atom([(F(0),F(1,2)),(F(1),F(1,2))],F(1,4))==F(1,4)
if __name__=='__main__':
    test_bounds()
    print('PASS: 4830 exact rational cases')
