import unittest
from fractions import Fraction as F

def cvar(v, alpha, a, b):
    assert F(0) <= v <= F(1) and F(0) <= alpha < F(1) and a < b
    return a + (b-a)*min(F(1), v/(1-alpha))

def bounds(lo, hi, rho, delta, alpha, a, b):
    assert F(0) <= lo <= hi <= F(1) and rho >= 0 and delta > 0
    return (cvar(max(F(0),lo-rho/delta),alpha,a,b),
            cvar(min(F(1),hi+rho/delta),alpha,a,b))

def reach_radius(hi, delta, alpha, a, b, target):
    assert a <= target <= b
    return delta*max(F(0),(1-alpha)*(target-a)/(b-a)-hi)

class TestIntervalTransportCVaR(unittest.TestCase):
    def test_envelope(self):
        self.assertEqual(bounds(F(1,8),F(1,4),F(1,8),F(1),F(1,2),F(0),F(4)),(F(0),F(3)))
    def test_inverse_radius(self):
        self.assertEqual(reach_radius(F(1,16),F(2),F(3,4),F(1),F(5),F(3)),F(1,8))
    def test_safety_boundary(self):
        self.assertEqual(bounds(F(0),F(1,16),F(1,8),F(2),F(3,4),F(1),F(5))[1],F(3))
        self.assertEqual(bounds(F(0),F(1,16),F(1,4),F(2),F(3,4),F(1),F(5))[1],F(4))
    def test_endpoint_monotonicity(self):
        for n in range(9):
            for m in range(n,9):
                lo,hi=F(n,8),F(m,8)
                lower,upper=bounds(lo,hi,F(1,16),F(1),F(1,2),F(0),F(2))
                self.assertLessEqual(lower,upper)
                self.assertEqual(upper,bounds(F(0),hi,F(1,16),F(1),F(1,2),F(0),F(2))[1])
    def test_lipschitz(self):
        for i in range(9):
            for j in range(9):
                x,y=F(i,8),F(j,8)
                rx=bounds(F(0),x,F(1,16),F(1),F(1,2),F(0),F(2))[1]
                ry=bounds(F(0),y,F(1,16),F(1),F(1,2),F(0),F(2))[1]
                self.assertLessEqual(abs(rx-ry),F(4)*abs(x-y))
    def test_example_six(self):
        self.assertEqual(bounds(F(0),F(1,8),F(0),F(1),F(1,2),F(0),F(2))[1],F(1,2))
        self.assertEqual(bounds(F(0),F(1,4),F(0),F(1),F(1,2),F(0),F(2))[1],F(1))
if __name__ == "__main__":
    unittest.main()
