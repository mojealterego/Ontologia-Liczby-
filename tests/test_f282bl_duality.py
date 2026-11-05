from fractions import Fraction as F
from itertools import product
import unittest

def tail(xs, ps, t):
    left=t; total=F(0)
    for x,p in sorted(zip(xs,ps),reverse=True):
        q=min(left,p); total+=q*x;left-=q
        if not left:break
    return total

def dual(xs,ps,t,z):
    return t*z+sum(p*max(F(0),x-z) for x,p in zip(xs,ps))

class TestDuality(unittest.TestCase):
    def test_exact_duality(self):
        checked=0
        for p,q,t in product([F(1,4),F(1,2),F(3,4)], [F(-2),F(0),F(3)], [F(1,4),F(1,2),F(3,4),F(1)]):
            xs=[q,q+4];ps=[p,1-p]
            self.assertEqual(tail(xs,ps,t),min(dual(xs,ps,t,z) for z in xs));checked+=1
        self.assertEqual(checked,36)
    def test_certificate(self):
        xs=[F(0),F(4)];ps=[F(1,2),F(1,2)];t=F(1,2)
        lower=F(1)
        self.assertLessEqual(lower,tail(xs,ps,t))
        self.assertLessEqual(tail(xs,ps,t),dual(xs,ps,t,F(0)))
    def test_lipschitz(self):
        for p,t in product([F(1,4),F(1,2),F(3,4)], [F(1,4),F(1,2),F(1)]):
            a=[F(0),F(4)];b=[F(1,10),F(39,10)];ps=[p,1-p]
            self.assertLessEqual(abs(tail(a,ps,t)-tail(b,ps,t)),t/F(10))
    def test_threshold_nonunique(self):
        xs=[F(0),F(2)];ps=[F(1,2),F(1,2)]
        for z in [F(0),F(1),F(2)]:
            self.assertEqual(dual(xs,ps,F(1,2),z),F(1))
if __name__=='__main__':unittest.main()
