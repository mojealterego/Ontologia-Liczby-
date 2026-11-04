import unittest
from fractions import Fraction as F

def cvar(p, losses, alpha):
    h=1-alpha
    if not (F(0)<h<=F(1)) or len(p)!=len(losses) or sum(p)!=1 or any(x<0 for x in p):
        raise ValueError("invalid distribution or alpha")
    remain=h
    total=F(0)
    for loss,prob in sorted(zip(losses,p),reverse=True):
        mass=min(remain,prob)
        total+=mass*loss
        remain-=mass
        if remain==0: break
    return total/h

class TestF282AT(unittest.TestCase):
    def test_box_extrema(self):
        p=[F(3,4),F(1,4)]; ell=[F(0),F(8)]; d=[F(2),F(1)]
        self.assertEqual(cvar(p,[x+y for x,y in zip(ell,d)],F(1,2)),F(11,2))
        self.assertEqual(cvar(p,[x-y for x,y in zip(ell,d)],F(1,2)),F(5,2))
    def test_subadditivity_strict(self):
        p=[F(1,2)]*2
        self.assertEqual(cvar(p,[F(1),F(0)],F(1,2))+cvar(p,[F(0),F(1)],F(1,2)),2)
        self.assertEqual(cvar(p,[F(1),F(1)],F(1,2)),1)
    def test_nonsharp_bound(self):
        p=[F(1,2)]*2
        self.assertEqual(cvar(p,[F(10),F(1)],F(1,2))-cvar(p,[F(10),F(0)],F(1,2)),0)
    def test_translation(self):
        p=[F(1,3)]*3
        for alpha in [F(0),F(1,2),F(9,10)]:
            self.assertEqual(cvar(p,[F(2),F(5),F(-1)],alpha)+3,cvar(p,[F(5),F(8),F(2)],alpha))
    def test_monotonicity_exhaustive(self):
        p=[F(1,2)]*2
        for a in range(-2,3):
            for b in range(-2,3):
                for da in range(3):
                    for db in range(3):
                        self.assertLessEqual(cvar(p,[F(a),F(b)],F(1,2)),cvar(p,[F(a+da),F(b+db)],F(1,2)))
    def test_weighted_l1_bound(self):
        p=[F(1,3)]*3; alpha=F(1,2)
        for j in range(3):
            x=[F(0)]*3; y=x.copy(); y[j]=F(1)
            self.assertLessEqual(abs(cvar(p,x,alpha)-cvar(p,y,alpha)),min(F(1),sum(p[i]*abs(x[i]-y[i]) for i in range(3))/(1-alpha)))
if __name__=="__main__":
    unittest.main()
