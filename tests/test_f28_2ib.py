import unittest
from fractions import Fraction as F

def bounds(g, lo, hi):
    assert len(g) == len(lo) == len(hi) and all(x > 0 for x in g)
    assert all(a <= b for a,b in zip(lo,hi))
    L=max([F(0)]+[max(F(0),a)/d for a,d in zip(lo,g)])
    U=max([F(0)]+[max(F(0),b)/d for b,d in zip(hi,g)])
    return L,U

class CertTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(bounds([F(2),F(3)],[F(1),F(1)],[F(1),F(2)]),(F(1,2),F(2,3)))
    def test_exact(self):
        self.assertEqual(bounds([F(2),F(3)],[F(1),F(2)],[F(1),F(2)]),(F(2,3),F(2,3)))
    def test_zero(self):
        self.assertEqual(bounds([F(1)],[F(-2)],[F(0)]),(F(0),F(0)))
    def test_exhaustive(self):
        n=0
        for g1 in range(1,5):
            for g2 in range(1,5):
                for b1 in range(-3,4):
                    for b2 in range(-3,4):
                        for e in range(4):
                            lo=[F(b1-e),F(b2-e)]
                            hi=[F(b1+e),F(b2+e)]
                            q=max(F(0),F(max(0,b1),g1),F(max(0,b2),g2))
                            L,U=bounds([F(g1),F(g2)],lo,hi)
                            self.assertLessEqual(L,q)
                            self.assertLessEqual(q,U)
                            n+=1
        self.assertEqual(n,3136)
if __name__ == '__main__':
    unittest.main()
