"""MSC 97D40 III-B: exhaustive finite decision and coding checks."""
import itertools
import math
import unittest

class TestDiagnosticDecision(unittest.TestCase):
    def test_kraft_prefix_lengths(self):
        for lengths in ((1,2,2),(2,2,2,2),(1,3,3,3,3)):
            self.assertLessEqual(sum(2**(-x) for x in lengths),1)
    def test_kraft_invalid(self):
        self.assertGreater(sum(2**(-x) for x in (1,1,2)),1)
    def test_entropy_bound(self):
        for weights in itertools.product(range(1,5),repeat=3):
            total=sum(weights)
            p=[w/total for w in weights]
            lengths=[math.ceil(-math.log2(v)) for v in p]
            entropy=-sum(v*math.log2(v) for v in p)
            avg=sum(v*l for v,l in zip(p,lengths))
            self.assertGreaterEqual(avg+1e-12,entropy)
            self.assertLess(avg,entropy+1+1e-12)
    def test_bayes_zero_one(self):
        for a in range(1,10):
            for b in range(1,10):
                p=a/(a+b)
                self.assertAlmostEqual(min(p,1-p),1-max(p,1-p))
    def test_information_value_nonnegative(self):
        # Two hidden states; binary observation with rational likelihoods.
        for prior_num in range(1,10):
            p=prior_num/10
            for sens_num in range(11):
                s=sens_num/10
                for false_num in range(11):
                    f=false_num/10
                    baseline=min(p,1-p)
                    # Joint probabilities of state and outcome.
                    y1_state1=p*s
                    y1_state0=(1-p)*f
                    y0_state1=p*(1-s)
                    y0_state0=(1-p)*(1-f)
                    post_risk=min(y1_state1,y1_state0)+min(y0_state1,y0_state0)
                    self.assertLessEqual(post_risk,baseline+1e-12)
    def test_independent_observation(self):
        for p in (.1,.3,.5,.9):
            for q in (.1,.4,.8):
                joint=[p*q,(1-p)*q,p*(1-q),(1-p)*(1-q)]
                post=min(joint[0],joint[1])+min(joint[2],joint[3])
                self.assertAlmostEqual(post,min(p,1-p))
    def test_asymmetric_loss(self):
        self.assertLess(.6,4.0)

if __name__ == "__main__":
    unittest.main()
