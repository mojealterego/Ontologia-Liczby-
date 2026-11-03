import unittest
from fractions import Fraction as F

def certificate(q, eps):
    assert len(q) == len(eps) and len(q)>0
    assert all(F(0)<=v<F(1) for v in q)
    assert all(v>=0 for v in eps)
    Q=F(1); E=F(0)
    for qi,ei in zip(q,eps):
        Q*=qi
        E=qi*E+ei
    return Q,E

def bounds(r,Q,E):
    return max(F(0),r-E)/(1+Q),(r+E)/(1-Q)

class CycleTests(unittest.TestCase):
    def test_weights(self):
        self.assertEqual(certificate([F(1,2),F(1,3)],[F(1,10),F(1,20)]),(F(1,6),F(1,12)))
    def test_bounds(self):
        self.assertEqual(bounds(F(1),F(1,6),F(1,12)),(F(11,14),F(13,10)))
    def test_actual_inside(self):
        lo,hi=bounds(F(1),F(1,6),F(1,12))
        self.assertLessEqual(lo,F(6,5))
        self.assertLessEqual(F(6,5),hi)
    def test_recurrence(self):
        self.assertEqual(F(1,4)**2*2+F(1,8)*(1+F(1,4)),F(9,32))
    def test_last_error(self):
        self.assertEqual(certificate([F(0),F(0)],[F(0),F(1)]),(F(0),F(1)))
    def test_parametric_exact(self):
        for a in range(1,7):
            for b in range(1,7):
                q=[F(a,10),F(b,10)]
                eps=[F(a,100),F(b,100)]
                Q,E=certificate(q,eps)
                self.assertEqual(E,q[1]*eps[0]+eps[1])
                self.assertEqual(Q,q[0]*q[1])

if __name__=="__main__":
    unittest.main()
