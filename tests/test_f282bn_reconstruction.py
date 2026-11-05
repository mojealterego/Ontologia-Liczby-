from fractions import Fraction as F
from itertools import product
import unittest

def H(d,t):
    left=t; ans=F(0)
    for x,p in sorted(d.items(), reverse=True):
        w=min(left,p);ans+=x*w;left-=w
        if not left:break
    return ans

def interp(d,u,v,t):
    return H(d,u)+(H(d,v)-H(d,u))*(t-u)/(v-u)

class TestBN(unittest.TestCase):
    def test_interpolation_bound(self):
        count=0
        for p,a,b in product([F(1,4),F(1,2),F(3,4)],[-3,0],[2,7]):
            d={F(a):p,F(b):1-p}
            for j in range(9):
                t=F(j,8)
                self.assertLessEqual(abs(H(d,t)-interp(d,F(0),F(1),t)),F(b-a,4))
                count+=1
        self.assertEqual(count,108)
    def test_sharpness(self):
        d={F(0):F(1,2),F(8):F(1,2)}
        self.assertEqual(H(d,F(1,2))-interp(d,F(0),F(1),F(1,2)),F(2))
    def test_transport_example(self):
        d={F(0):F(1)};e={F(0):F(3,4),F(4):F(1,4)}
        self.assertEqual(max(abs(H(d,F(i,8))-H(e,F(i,8))) for i in range(9)),F(1))
    def test_slope_noise(self):
        u,v=F(1,10),F(3,10);delta=F(1,100);x=F(5)
        noisy_slope=((x*v-delta)-(x*u+delta))/(v-u)
        self.assertEqual(abs(noisy_slope-x),2*delta/(v-u))

if __name__=='__main__':unittest.main()
