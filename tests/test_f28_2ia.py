import unittest
from fractions import Fraction as F
from itertools import product

def bounds(g, samples, epsilon):
    a = max(-z for z in samples)
    return max(a, F(0))/g, max(a+epsilon, F(0))/g

class TestDirectionalCertificates(unittest.TestCase):
    def test_grid_certificates(self):
        count=0
        for g, lo, hi in product(range(1,8), range(-5,1), range(1,6)):
            K=[F(lo),F(hi)]
            S=[F(hi)]
            epsilon=F(hi-lo)
            L,U=bounds(F(g),S,epsilon)
            q=max(F(0),-min(K))/g
            self.assertLessEqual(L,q)
            self.assertLessEqual(q,U)
            count+=1
        self.assertEqual(count,210)

    def test_exact_extreme(self):
        self.assertEqual(bounds(F(2),[F(-3),F(1)],F(0)),(F(3,2),F(3,2)))

    def test_invisible_direction(self):
        self.assertEqual(bounds(F(1),[F(1),F(2)],F(0)),(0,0))

    def test_refinement(self):
        old=bounds(F(2),[F(0)],F(3))
        new=bounds(F(2),[F(-2),F(0)],F(1))
        self.assertLessEqual(old[0],new[0])
        self.assertLessEqual(new[1],old[1])

if __name__=="__main__":
    unittest.main()
