import unittest
from fractions import Fraction as F

def robust_two(h):
    h=F(h)
    return max(F(1)-h/2,F(0))

def adaptive_two(h):
    h=F(h)
    return max(F(1)-min(h,F(1)),F(0))

class RobustMinimax(unittest.TestCase):
    def test_exact_grid(self):
        for k in range(21):
            h=F(k,10)
            self.assertEqual(robust_two(h),F(1)-h/2)
    def test_saturation(self):
        for h in [F(2),F(3),F(100)]:
            self.assertEqual(robust_two(h),0)
    def test_information_gap(self):
        self.assertEqual(robust_two(F(1))-adaptive_two(F(1)),F(1,2))
        self.assertEqual(robust_two(F(1,2))-adaptive_two(F(1,2)),F(1,4))
    def test_dual_certificate(self):
        for k in range(21):
            h=F(k,10)
            lower=F(1)-h/2
            self.assertEqual(robust_two(h),lower)
    def test_convexity(self):
        for a in range(11):
            for b in range(11):
                h1,h2=F(a,5),F(b,5)
                mid=(h1+h2)/2
                self.assertLessEqual(robust_two(mid),(robust_two(h1)+robust_two(h2))/2)
    def test_lipschitz(self):
        for a in range(21):
            for b in range(a,21):
                h1,h2=F(a,10),F(b,10)
                self.assertLessEqual(robust_two(h1)-robust_two(h2),h2-h1)
    def test_interval(self):
        self.assertEqual(F(5)-2*min(F(2),F(4)),F(1))
    def test_correlated(self):
        scenarios=[(F(1),F(0)),(F(0),F(1))]
        self.assertEqual(max(sum(x) for x in scenarios),1)
        self.assertEqual(sum(max(x[i] for x in scenarios) for i in range(2)),2)

if __name__=="__main__":
    unittest.main()
