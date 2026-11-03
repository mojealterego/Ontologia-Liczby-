import unittest
from fractions import Fraction as Q

def project_interval(x, lower=None, upper=None):
    if lower is not None: x=max(x,lower)
    if upper is not None: x=min(x,upper)
    return x

class AlternatingProjections(unittest.TestCase):
    def test_z1(self):
        x=Q(3); y=project_interval(x,upper=Q(1)); self.assertEqual(project_interval(y,lower=Q(0)),1)
    def test_z2(self):
        x=Q(-2); y=project_interval(x,upper=Q(1)); self.assertEqual(project_interval(y,lower=Q(0)),0)
    def test_z3(self):
        self.assertEqual(project_interval(Q(7),lower=Q(0),upper=Q(0)),0)
    def test_z4(self):
        self.assertEqual(project_interval(Q(1,2),lower=Q(0),upper=Q(1)),Q(1,2))
    def test_z5(self):
        self.assertEqual(project_interval(Q(0),lower=Q(2)),2)
    def test_z7(self):
        self.assertEqual(Q(6)**2/9,4)
    def test_z8(self):
        self.assertEqual(1-Q(1,2)**2,Q(3,4))
    def test_z9(self):
        self.assertEqual(16*Q(3,4)**2,9)
    def test_z11(self):
        self.assertEqual(project_interval(Q(-2),lower=Q(1),upper=Q(3)),1)
    def test_z12(self):
        self.assertEqual(project_interval(Q(5),lower=Q(1),upper=Q(3)),3)
    def test_nonexpansiveness_intervals(self):
        for a in range(-5,6):
            for b in range(-5,6):
                self.assertLessEqual(abs(project_interval(a,0,2)-project_interval(b,0,2)),abs(a-b))

if __name__=="__main__": unittest.main()
