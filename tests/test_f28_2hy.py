import unittest
from fractions import Fraction as F

def certificate(g, scenarios, delta):
    g=F(g); delta=F(delta)
    q=max([F(0)]+[max(F(0),-F(s)/g) for s in scenarios])
    return q,q+delta/g

class CertificateTests(unittest.TestCase):
    def test_exact_grid(self):
        count=0
        for g in range(1,12):
            for a in range(-8,9):
                for b in range(a,9):
                    S=[F(a)]
                    K=[F(a),F(b)]
                    delta=F(b-a)
                    lo,hi=certificate(g,S,delta)
                    actual=max(F(0),-F(a,g),-F(b,g))
                    self.assertLessEqual(lo,actual)
                    self.assertLessEqual(actual,hi)
                    count+=1
        self.assertEqual(count,1683)
    def test_tight(self):
        self.assertEqual(certificate(2,[0],1),(F(0),F(1,2)))
    def test_radius(self):
        lo,hi=certificate(4,[-1],1)
        self.assertEqual((1/hi,1/lo),(F(2),F(4)))
    def test_nested(self):
        self.assertLessEqual(certificate(2,[0],1)[0],certificate(2,[0,-1],0)[0])

if __name__=="__main__":
    unittest.main()
