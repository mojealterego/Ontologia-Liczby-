import unittest
from fractions import Fraction as F

class TestWassersteinTail(unittest.TestCase):
    def test_sharpness(self):
        for t in (F(i,20) for i in range(1,21)):
            for d in (F(1,3), F(2), F(5)):
                self.assertEqual((t*d)/t,d)

    def test_tail_integrals(self):
        def H(atoms,t):
            rem=t; value=F(0)
            for x,p in sorted(atoms,reverse=True):
                take=min(rem,p)
                value+=take*x
                rem-=take
                if not rem: break
            return value
        nu=[(F(2),F(3,4)),(F(6),F(1,4))]
        self.assertEqual(H(nu,F(1,10)),F(3,5))
        self.assertEqual(H(nu,F(1,2)),F(2))

    def test_uniform_budget_bound(self):
        def H(atoms,t):
            rem=t;value=F(0)
            for x,p in sorted(atoms,reverse=True):
                take=min(rem,p);value+=take*x;rem-=take
                if not rem:break
            return value
        mu=[(F(0),F(1))]
        for i in range(1,20):
            t=F(i,20)
            nu=[(F(0),1-t),(F(1),t)]
            for j in range(21):
                s=F(j,20)
                self.assertLessEqual(abs(H(mu,s)-H(nu,s)),t)

if __name__=="__main__":
    unittest.main()
