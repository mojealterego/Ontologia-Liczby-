"""Exact-arithmetic checks for F28.2-AD; not a formal proof."""
import unittest
from fractions import Fraction as F

def certificate(L, u, i):
    m = len(L)
    q = F(1)
    for x in L:
        q *= x
    if q >= 1:
        raise ValueError("full cycle must be contractive")
    b, p = F(0), F(1)
    for k in range(m):
        b += p * u[(i - 1 - k) % m]
        p *= L[(i - 1 - k) % m]
    return b / (1 - q)

class TestF282AD(unittest.TestCase):
    def test_example(self):
        L, u = [F(2), F(1,4)], [F(1,2), F(1,4)]
        self.assertEqual(certificate(L,u,0), F(3,4))
        self.assertEqual(certificate(L,u,1), F(2))
    def test_budget(self):
        L = [F(2), F(1,4)]
        self.assertEqual(certificate(L,[F(1,2),F(0)],0),F(1,4))
        self.assertEqual(certificate(L,[F(1,4),F(0)],0),F(1,8))
    def test_sharpness(self):
        for a in range(1,9):
            for b in range(1,9):
                L, u = [F(a,10),F(b,10)], [F(a,7),F(b,11)]
                y = [certificate(L,u,i) for i in range(2)]
                self.assertEqual(y[1]-L[0]*y[0],u[0])
                self.assertEqual(y[0]-L[1]*y[1],u[1])
    def test_monotonicity(self):
        L, a = [F(3,2),F(1,3),F(1,4)], [F(1),F(2),F(3)]
        for i in range(3):
            self.assertLessEqual(certificate(L,a,i),certificate(L,[x+1 for x in a],i))
    def test_single_phase_lower(self):
        self.assertEqual(F(3,2)/(1+F(1,2)),1)

if __name__ == "__main__":
    unittest.main()
