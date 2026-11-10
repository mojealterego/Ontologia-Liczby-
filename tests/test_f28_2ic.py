from fractions import Fraction as F
import unittest

def bounds(edges):
    L=max([F(0)]+[max(F(0),l)/g for g,l,u,h in edges])
    U=max([F(0)]+[max(F(0),u)/g for g,l,u,h in edges])
    q=max([F(0)]+[max(F(0),h)/g for g,l,u,h in edges])
    return L,q,U

class CertificateTests(unittest.TestCase):
    def test_grid_exact(self):
        count=0
        for g in range(1,7):
            for l in range(-3,4):
                for h in range(l,4):
                    for u in range(h,5):
                        L,q,U=bounds([(F(g),F(l),F(u),F(h))])
                        self.assertLessEqual(L,q)
                        self.assertLessEqual(q,U)
                        if L>0:
                            self.assertLessEqual(1/U,1/q)
                            self.assertLessEqual(1/q,1/L)
                        count+=1
        self.assertGreater(count,1000)
    def test_two_edges(self):
        L,q,U=bounds([(F(1),F(1),F(2),F(3,2)),(F(2),F(3),F(4),F(7,2))])
        self.assertEqual((L,q,U),(F(3,2),F(7,4),F(2)))
    def test_relative(self):
        L,q,U=bounds([(F(1),F(4,5),F(1),F(9,10))])
        self.assertLessEqual(U,F(5,4)*L)
    def test_monotonic(self):
        a=bounds([(F(1),F(1),F(3),F(7,4))])
        b=bounds([(F(1),F(3,2),F(2),F(7,4))])
        self.assertLessEqual(a[0],b[0])
        self.assertGreaterEqual(a[2],b[2])

if __name__=="__main__":
    unittest.main()
