import unittest
from fractions import Fraction as F

def cert(q,a,m,n,R):
    p=F(1)
    for i in range(m,n): p*=q[i]
    s=p*R
    for j in range(m,n):
        w=F(1)
        for i in range(j+1,n): w*=q[i]
        s+=w*a[j]
    return s

class DelayedObservations(unittest.TestCase):
    def test_z2(self):
        self.assertEqual(cert([F(1,2)]*2,[F(1,4)]*2,0,2,F(4)),F(11,8))
    def test_z3(self):
        self.assertEqual(cert([F(1,2)]*2,[F(0),F(1,4)],1,2,F(1)),F(3,4))
    def test_z5(self):
        self.assertEqual(F(1,5)+F(1,10)+F(1,20),F(7,20))
    def test_z6(self):
        self.assertEqual(cert([F(1,2)]*3,[F(1,4)]*3,0,3,F(2)),F(11,16))
    def test_z8(self):
        self.assertEqual(cert([F(1,2),F(1,3)],[F(1),F(1,2)],0,2,F(6)),F(11,6))
    def test_z9(self):
        q=[F(1,2)]*2;a=[F(0)]*2
        self.assertEqual(cert(q,a,0,2,F(6,5))-cert(q,a,0,2,F(1)),F(1,20))
    def test_sharpness_grid(self):
        for q0 in [F(0),F(1,4),F(1,2),F(3,4)]:
            for q1 in [F(0),F(1,3),F(2,3)]:
                for a0 in [F(0),F(1,5)]:
                    for a1 in [F(0),F(1,7)]:
                        x=F(2)
                        x=q0*x+a0
                        x=q1*x+a1
                        self.assertEqual(x,cert([q0,q1],[a0,a1],0,2,F(2)))
    def test_minimum_observations(self):
        q=[F(1,2)]*2;a=[F(1,4)]*2
        self.assertEqual(min(cert(q,a,0,2,F(4)),cert(q,a,1,2,F(1))),F(3,4))

if __name__=="__main__": unittest.main()
