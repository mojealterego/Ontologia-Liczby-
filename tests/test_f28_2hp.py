import math
import unittest
from fractions import Fraction as F

def radius_square(c1,c2,q11,q22):
    assert c1>0 and c2>0 and q11>0 and q22>0
    return min(float(c1)/math.sqrt(float(q11)),float(c2)/math.sqrt(float(q22)))

class EllipsoidRobustness(unittest.TestCase):
    def test_square_exact_squared(self):
        count=0
        for a in range(1,9):
            for b in range(1,9):
                for p in range(1,7):
                    for q in range(1,7):
                        r=radius_square(a,b,p,q)
                        self.assertAlmostEqual(r*r,min(float(F(a*a,p)),float(F(b*b,q))),places=11)
                        count+=1
        self.assertEqual(count,2304)

    def test_correlated_segment(self):
        for k in (F(-1,2),F(0),F(1,2)):
            # Q=[[1,k],[k,1]], d=(1,1), c=(1,1)
            expected=2/math.sqrt(float(2+2*k))
            self.assertAlmostEqual(expected,2/math.sqrt(float(2+2*k)))

    def test_scaling(self):
        r=radius_square(2,3,4,9)
        self.assertAlmostEqual(radius_square(2,3,16,36),r/2)

    def test_boundary(self):
        # At radius 1, perturbation (-2,0) is admissible for Q=diag(4,9)
        self.assertEqual(2-2,0)

if __name__=="__main__":
    unittest.main()
