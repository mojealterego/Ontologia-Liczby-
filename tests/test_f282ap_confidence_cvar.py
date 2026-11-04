import unittest
from fractions import Fraction as F

def risk(a,b,u,alpha):
    assert a<b and 0<=u<=1 and 0<=alpha<1
    return a+(b-a)*min(F(1),u/(1-alpha))

class TestConfidenceProfile(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(risk(F(0),F(10),F(1,5),F(1,2)),4)
        self.assertEqual(risk(F(0),F(10),F(1,5),F(4,5)),10)
    def test_monotonicity(self):
        for u in [F(0),F(1,8),F(1,2),F(1)]:
            vals=[risk(F(0),F(8),u,F(i,20)) for i in range(20)]
            self.assertEqual(vals,sorted(vals))
    def test_threshold(self):
        for i in range(20):
            alpha=F(i,20)
            self.assertEqual(risk(F(0),F(10),F(1,5),alpha)<=5,alpha<=F(3,5))
    def test_lipschitz(self):
        for i in range(19):
            x,y=F(i,20),F(i+1,20)
            u=F(1,5)
            lhs=risk(F(0),F(10),u,y)-risk(F(0),F(10),u,x)
            rhs=10*u*(y-x)/((1-x)*(1-y))
            self.assertTrue(0<=lhs<=rhs)
    def test_joint(self):
        for i in range(10):
            u,v=F(i,10),F(i+1,10)
            a,b=F(i,20),F(i+1,20)
            lhs=abs(risk(F(0),F(10),u,a)-risk(F(0),F(10),v,b))
            rhs=10*(abs(u-v)/(1-a)+v*abs(a-b)/((1-a)*(1-b)))
            self.assertLessEqual(lhs,rhs)
    def test_counterexample_convexity(self):
        self.assertGreater(risk(F(0),F(4),F(1,2),F(1,2)),(risk(F(0),F(4),F(1,2),F(0))+2*risk(F(0),F(4),F(1,2),F(3,4)))/3)

if __name__=="__main__": unittest.main()
