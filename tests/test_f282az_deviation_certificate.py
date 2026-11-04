import unittest
from fractions import Fraction as F
from itertools import product

def cvar(p,x,h):
    rem=h; total=F(0)
    for v,w in sorted(zip(x,p),reverse=True):
        take=min(rem,w);total+=take*v;rem-=take
        if rem==0:break
    return total/h

def aggregate(p,x,blocks):
    m=list(x)
    for block in blocks:
        weight=sum((p[i] for i in block),F(0))
        avg=sum((p[i]*x[i] for i in block),F(0))/weight
        for i in block:m[i]=avg
    return m

def budget(p,x,m):
    return sum((w*max(F(0),a-b) for w,a,b in zip(p,x,m)),F(0))

class TestAZ(unittest.TestCase):
    def test_two_point_exhaustive(self):
        for a,b in product(range(-2,3),repeat=2):
            for n in range(1,8):
                p=[F(n,8),F(8-n,8)];x=[F(a),F(b)]
                m=aggregate(p,x,[[0,1]]);B=budget(p,x,m)
                self.assertEqual(2*B,sum((w*abs(v-u) for w,v,u in zip(p,x,m)),F(0)))
                for h in [F(1),F(3,4),F(1,2),F(1,4),F(1,8)]:
                    gap=cvar(p,x,h)-cvar(p,m,h)
                    self.assertGreaterEqual(gap,0)
                    self.assertLessEqual(gap,min(max(abs(v-u) for v,u in zip(x,m)),B/h))
    def test_four_point(self):
        p=[F(1,4)]*4
        for vals in product(range(3),repeat=4):
            x=list(map(F,vals))
            for blocks in [[[0,1],[2,3]],[[0,1,2,3]],[[0],[1],[2],[3]]]:
                m=aggregate(p,x,blocks)
                for h in [F(1),F(1,2),F(1,4)]:
                    gap=cvar(p,x,h)-cvar(p,m,h)
                    self.assertGreaterEqual(gap,0)
                    self.assertLessEqual(gap,budget(p,x,m)/h)
    def test_sharpness(self):
        for n in range(1,10):
            h=F(n,10);p=[1-h,h];x=[F(0),F(1)]
            m=aggregate(p,x,[[0,1]])
            self.assertEqual(cvar(p,x,h)-cvar(p,m,h),budget(p,x,m)/h)
    def test_stability(self):
        p=[F(1,4)]*4;blocks=[[0,1],[2,3]]
        for k in range(100):
            x=[F((k+i*i)%7) for i in range(4)]
            y=[F((2*k+3*i)%11) for i in range(4)]
            lhs=abs(budget(p,x,aggregate(p,x,blocks))-budget(p,y,aggregate(p,y,blocks)))
            rhs=2*sum((w*abs(a-b) for w,a,b in zip(p,x,y)),F(0))
            self.assertLessEqual(lhs,rhs)

if __name__=="__main__":unittest.main()
