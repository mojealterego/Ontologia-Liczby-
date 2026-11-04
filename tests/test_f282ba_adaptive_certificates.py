from fractions import Fraction as F
import itertools, unittest
def cvar(p,x,h):
    remain=h; total=F(0)
    for value,mass in sorted(zip(x,p),reverse=True):
        take=min(remain,mass);total+=take*value;remain-=take
        if remain==0:break
    return total/h
def aggregate(p,x,blocks):
    y=list(x)
    for block in blocks:
        avg=sum((p[i]*x[i] for i in block),F(0))/sum((p[i] for i in block),F(0))
        for i in block:y[i]=avg
    return y
def budget(p,x,y):
    return sum((p[i]*max(F(0),x[i]-y[i]) for i in range(len(x))),F(0))
class TestBA(unittest.TestCase):
    def test_exact_certificates(self):
        for values in itertools.product(range(-2,3),repeat=3):
            p=[F(1,3)]*3;x=list(map(F,values))
            for blocks in [[[0,1,2]],[[0,1],[2]],[[0],[1,2]]]:
                y=aggregate(p,x,blocks)
                for h in [F(1),F(1,2),F(1,3),F(1,4)]:
                    gap=cvar(p,x,h)-cvar(p,y,h)
                    self.assertGreaterEqual(gap,0)
                    self.assertLessEqual(gap,budget(p,x,y)/h)
                    self.assertLessEqual(gap,max(abs(a-b) for a,b in zip(x,y)))
    def test_counterexamples(self):
        p=[F(1,3)]*3;x=list(map(F,[0,1,3]));y=aggregate(p,x,[[0,1],[2]])
        self.assertEqual(cvar(p,x,F(1,3))-cvar(p,y,F(1,3)),0)
        self.assertEqual(budget(p,x,y),F(1,6))
        p=[F(1,2)]*2;x=list(map(F,[0,2]));y=aggregate(p,x,[[0,1]])
        self.assertEqual(cvar(p,x,F(1,2))-cvar(p,y,F(1,2)),1)
        self.assertEqual(budget(p,x,y),F(1,2))
    def test_hierarchy(self):
        p=[F(1,4)]*4;x=list(map(F,[0,1,2,7]))
        fine=aggregate(p,x,[[0,1],[2],[3]])
        coarse=aggregate(p,x,[[0,1,2,3]])
        for h in [F(1),F(3,4),F(1,2),F(1,4)]:
            self.assertGreaterEqual(cvar(p,x,h),cvar(p,fine,h))
            self.assertGreaterEqual(cvar(p,fine,h),cvar(p,coarse,h))
if __name__=='__main__':unittest.main()
