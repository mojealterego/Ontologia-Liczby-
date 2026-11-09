from fractions import Fraction as F
import unittest

def radius(c, vertices):
    # P=[0,1]^n, x=0; vertices are perturbation vertices.
    assert all(a > 0 for a in c)
    bounds = []
    for i, a in enumerate(c):
        b = max(-v[i] for v in vertices)
        if b > 0:
            bounds.append(a / b)
    return min(bounds) if bounds else None

class PolyhedralRobustness(unittest.TestCase):
    def test_asymmetry(self):
        self.assertEqual(radius([F(2)], [(F(-3),),(F(1),),(F(0),)]), F(2,3))
    def test_invisible(self):
        self.assertIsNone(radius([F(1)], [(F(0),),(F(2),)]))
    def test_two_dimensional(self):
        k=[(F(0),F(0)),(F(-1),F(0)),(F(0),F(-2))]
        self.assertEqual(radius([F(2),F(5)],k),F(2))
        self.assertEqual(radius([F(2),F(5)],[(2*a,2*b) for a,b in k]),F(1))
    def test_grid_and_boundary(self):
        for a in range(1,12):
            for b in range(1,12):
                for p in range(1,8):
                    for q in range(1,8):
                        k=[(F(0),F(0)),(F(-p),F(0)),(F(0),F(-q))]
                        r=radius([F(a),F(b)],k)
                        self.assertEqual(r,min(F(a,p),F(b,q)))
                        for t in [r/2,r]:
                            margins=[F(a)-t*p,F(b)-t*q]
                            self.assertTrue(all(z>0 for z in margins) if t<r else any(z==0 for z in margins))
if __name__ == "__main__":
    unittest.main()
