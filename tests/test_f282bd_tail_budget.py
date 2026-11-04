import unittest
from fractions import Fraction as F

def H(values, weights, t):
    assert len(values)==len(weights) and sum(weights)==1 and F(0)<=t<=1
    left=t; total=F(0)
    for v,p in sorted(zip(values,weights),reverse=True):
        take=min(left,p)
        total+=take*v
        left-=take
        if left==0: break
    return total

class TailBudgetTests(unittest.TestCase):
    def test_exact_two_point(self):
        for k in range(101):
            t=F(k,100)
            self.assertEqual(H([F(0),F(10)],[F(1,2)]*2,t), min(10*t,F(5)))
    def test_concavity(self):
        vals=[F(-2),F(1),F(7)]; p=[F(1,4),F(1,2),F(1,4)]
        for i in range(21):
            for j in range(21):
                a,b=F(i,20),F(j,20)
                self.assertGreaterEqual(H(vals,p,(a+b)/2),(H(vals,p,a)+H(vals,p,b))/2)
    def test_ratio_monotonicity(self):
        vals=[F(-2),F(1),F(7)]; p=[F(1,4),F(1,2),F(1,4)]
        ratios=[H(vals,p,F(i,100))/F(i,100) for i in range(1,101)]
        self.assertTrue(all(a>=b for a,b in zip(ratios,ratios[1:])))
    def test_stability(self):
        p=[F(1,4),F(1,2),F(1,4)]
        x=[F(-2),F(1),F(7)]; y=[F(-3),F(2),F(6)]
        for i in range(101):
            t=F(i,100)
            self.assertLessEqual(abs(H(x,p,t)-H(y,p,t)),t)
    def test_endpoints(self):
        p=[F(1,4),F(1,2),F(1,4)]
        x=[F(-2),F(1),F(7)]
        self.assertEqual(H(x,p,F(0)),0)
        self.assertEqual(H(x,p,F(1)),F(7,4))
    def test_strict_excess(self):
        p=[F(1,4),F(1,2),F(1,4)]
        x=[F(-2),F(1),F(7)]
        for i in range(1,100):
            t=F(i,100)
            self.assertGreater(H(x,p,t)-t*F(7,4),0)

if __name__=="__main__":
    unittest.main()
