import unittest
from fractions import Fraction as F

class TestF282GK(unittest.TestCase):
    def test_moments(self):
        ew=F(1,12); ew2=F(1,80)
        self.assertEqual(ew2-ew*ew,F(1,180))
    def test_quadratic_exact(self):
        for n in range(1,30):
            h=F(1,n)
            variance=sum((h**6/F(180) for _ in range(n)),F(0))
            self.assertEqual(variance,F(1,180*n**5))
    def test_optimal_ratio(self):
        l1=l2=F(1,2)
        n1,n2=2,4
        b=lambda a,b: (l1**6/F(a**5)+F(64)*l2**6/F(b**5))/720
        self.assertLess(b(n1,n2),b(3,3))
        self.assertLess(b(n1,n2),b(1,5))
    def test_dependence_counterexample(self):
        independent=2*(F(1,8)**2)*F(1,180)
        dependent=(2*F(1,8))**2*F(1,180)
        self.assertEqual(dependent,2*independent)
        self.assertEqual(dependent,F(1,2880))
    def test_rounding_bound(self):
        for a in range(2,40):
            self.assertGreaterEqual(a//1,F(a,2))
if __name__=='__main__':
    unittest.main()
