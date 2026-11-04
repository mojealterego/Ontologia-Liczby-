import unittest
from fractions import Fraction as F

def cvar(p, losses, alpha):
    assert F(0) <= alpha < F(1)
    caps=[v/(1-alpha) for v in p]
    remaining=F(1)
    total=F(0)
    for i in sorted(range(len(losses)), key=lambda k: losses[k], reverse=True):
        take=min(remaining,caps[i])
        total+=take*losses[i]
        remaining-=take
    assert remaining==0
    return total

def w2(p,r):
    assert len(p)==len(r)==2
    return abs(p[1]-r[1])

class TransportCvarTests(unittest.TestCase):
    def test_t1_quantile(self):
        self.assertEqual(cvar([F(1,2),F(1,2)],[F(2),F(5)],F(1,2)),F(5))
    def test_t2_transport_grid(self):
        for a in [F(0),F(1,4),F(1,2),F(3,4)]:
            for i in range(9):
                for j in range(9):
                    p=[F(8-i,8),F(i,8)]
                    r=[F(8-j,8),F(j,8)]
                    diff=abs(cvar(p,[F(0),F(1)],a)-cvar(r,[F(0),F(1)],a))
                    self.assertLessEqual(diff,w2(p,r)/(1-a))
    def test_t4_sharp(self):
        for a in [F(0),F(1,4),F(1,2),F(3,4)]:
            e=(1-a)/2
            self.assertEqual(cvar([1-e,e],[F(0),F(1)],a),e/(1-a))
    def test_z2(self):
        self.assertEqual(cvar([F(7,8),F(1,8)],[F(0),F(4)],F(3,4)),F(2))
    def test_z6(self):
        for x in range(-8,9):
            self.assertEqual(cvar([F(1,2),F(1,2)],[F(x),F(-x)],F(1,2)),abs(x))
    def test_t5_loss_perturbation(self):
        for i in range(9):
            p=[F(8-i,8),F(i,8)]
            self.assertLessEqual(abs(cvar(p,[F(0),F(1)],F(1,2))-cvar(p,[F(1,5),F(6,5)],F(1,2))),F(1,5))

if __name__=="__main__":
    unittest.main()
