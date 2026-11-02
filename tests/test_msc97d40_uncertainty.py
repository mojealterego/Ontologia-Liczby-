"""MSC 97D40 III-C: uncertainty, group disparity, TV and robust risk."""
import itertools
import math
import unittest

def tv(p,q):
    return sum(abs(a-b) for a,b in zip(p,q))/2

def risk(p,loss):
    return sum(a*b for a,b in zip(p,loss))

class TestUncertaintyAndFairness(unittest.TestCase):
    def test_variance_bound_bernoulli(self):
        for i in range(101):
            p=i/100
            self.assertLessEqual(p*(1-p),.25+1e-12)
    def test_chebyshev_bound(self):
        n=100;eps=.2
        self.assertAlmostEqual(1/(4*n*eps**2),.0625)
    def test_union_bound(self):
        self.assertAlmostEqual(3/(4*100*.2**2),.1875)
    def test_disparity_reverse_triangle(self):
        for a,b,c,d in itertools.product((0,.25,.5,.75,1),repeat=4):
            self.assertLessEqual(abs(abs(a-b)-abs(c-d)),abs(a-c)+abs(b-d)+1e-12)
    def test_tv_bound_exhaustive(self):
        # Three-point distributions with denominators 4.
        distributions=[(a/4,b/4,(4-a-b)/4) for a in range(5) for b in range(5-a)]
        for p in distributions:
            for q in distributions:
                distance=tv(p,q)
                for bits in itertools.product((0,1),repeat=3):
                    self.assertLessEqual(abs(risk(p,bits)-risk(q,bits)),distance+1e-12)
    def test_tv_equality_example(self):
        p=(.7,.3);q=(.4,.6);loss=(0,1)
        self.assertAlmostEqual(tv(p,q),.3)
        self.assertAlmostEqual(abs(risk(p,loss)-risk(q,loss)),.3)
    def test_mixture(self):
        self.assertAlmostEqual(.2*.9+.8*.1,.26)
    def test_simpson_counterexample(self):
        a=.9*.8+.1*.1
        b=.1*.9+.9*.2
        self.assertGreater(a,b)
        self.assertLess(.8,.9)
        self.assertLess(.1,.2)
    def test_dependent_sample_variance(self):
        for n in range(2,50):
            self.assertGreater(.25,.25/n)
    def test_robust_upper_bound(self):
        for p in ((.2,.8),(.4,.6),(.7,.3)):
            for q in ((.1,.9),(.3,.7),(.5,.5),(.9,.1)):
                rho=tv(p,q)
                for loss in ((0,1),(1,0),(.25,.75)):
                    self.assertLessEqual(risk(q,loss),min(1,risk(p,loss)+rho)+1e-12)

if __name__=="__main__":
    unittest.main()
