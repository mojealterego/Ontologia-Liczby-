"""Exact rational regression tests for F28.2-X."""
import unittest
from fractions import Fraction as F

def interval(r, eta, q):
    assert 0 <= q < 1 and r >= 0 and eta >= 0
    return max(F(0), r - eta)/(1+q), (r+eta)/(1-q)

def multi(readings, q):
    assert readings and 0 <= q < 1
    a = max(max(F(0), r-e) for r,e in readings)
    b = min(r+e for r,e in readings)
    if a > b:
        raise ValueError("inconsistent measurements")
    return a/(1+q), b/(1-q)

class Certificates(unittest.TestCase):
    def test_z1(self): self.assertEqual(interval(F(3,4),F(1,8),F(1,2)),(F(5,12),F(7,4)))
    def test_z2(self): self.assertEqual(interval(F(1,6),F(1,6),F(1,3)),(F(0),F(1,2)))
    def test_z3(self): self.assertEqual(multi([(F(1),F(1,4)),(F(9,8),F(1,8))],F(1,2)),(F(2,3),F(5,2)))
    def test_z4(self): self.assertEqual(F(1,25)+F(1,100),(1-F(1,2))*F(1,10))
    def test_z5(self):
        for n in range(12):
            bound=F(1,2)**n+sum(F(1,2)**(n-1-j)*F(1,16) for j in range(n))
            self.assertEqual(bound,F(1,8)+F(7,8)*F(1,2)**n)
    def test_z6(self): self.assertEqual(interval(F(1),F(0),F(1,4)),(F(4,5),F(4,3)))
    def test_z7(self):
        with self.assertRaises(ValueError): multi([(F(1),F(0)),(F(2),F(0))],F(1,2))
    def test_z8(self): self.assertEqual(interval(F(1,4),F(0),F(3,4)),(F(1,7),F(1)))
    def test_sharpness(self):
        for q in (F(0),F(1,4),F(1,2),F(9,10)):
            lower,upper=interval(F(1),F(0),q)
            self.assertEqual(lower,1/(1+q))
            self.assertEqual(upper,1/(1-q))
    def test_monotonicity(self):
        for r in (F(0),F(1,2),F(2)):
            for eta in (F(0),F(1,4)):
                l1,u1=interval(r,eta,F(1,4))
                l2,u2=interval(r,eta,F(3,4))
                self.assertGreaterEqual(l1,l2)
                self.assertLessEqual(u1,u2)

if __name__ == "__main__":
    unittest.main()
