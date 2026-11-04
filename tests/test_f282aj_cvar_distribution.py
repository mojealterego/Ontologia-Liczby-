import unittest
from fractions import Fraction as F

def cvar_two(high_probability, high_loss, alpha):
    if not (F(0) <= high_probability <= 1 and F(0) <= alpha < 1):
        raise ValueError("invalid probability or alpha")
    return high_loss * min(F(1), high_probability / (1-alpha))

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

class TestF282AJ(unittest.TestCase):
    def test_exact_example(self):
        self.assertEqual(cvar_two(F(1,4),F(8),F(1,2)), F(4))
    def test_sharp_tv(self):
        for a in (F(0),F(1,4),F(1,2),F(3,4)):
            for d in (F(1,16),F(1,8),F(1,4)):
                if d<=1-a:
                    self.assertEqual(cvar_two(d,F(1),a),d/(1-a))
    def test_bound(self):
        for a in (F(0),F(1,4),F(1,2),F(3,4)):
            for p in (F(0),F(1,8),F(1,4),F(1,2),F(1)):
                for q in (F(0),F(1,8),F(1,4),F(1,2),F(1)):
                    left=abs(cvar_two(p,F(8),a)-cvar_two(q,F(8),a))
                    self.assertLessEqual(left,min(F(8),F(8)*abs(p-q)/(1-a)))
    def test_tv(self):
        self.assertEqual(tv((F(1,4),F(3,4)),(F(0),F(1))),F(1,4))
    def test_robust_example(self):
        self.assertEqual(cvar_two(F(3,8),F(8),F(1,2)),F(6))
    def test_joint_lipschitz(self):
        for p in (F(0),F(1,4),F(1,2),F(1)):
            for q in (F(0),F(1,4),F(1,2),F(1)):
                left=abs(cvar_two(p,F(8),F(1,2))-cvar_two(q,F(9),F(1,2)))
                self.assertLessEqual(left,F(1)+F(9)*abs(p-q)/F(1,2))
    def test_constant_loss(self):
        self.assertEqual(cvar_two(F(1),F(3),F(3,4)),F(3))

if __name__=="__main__":
    unittest.main()
