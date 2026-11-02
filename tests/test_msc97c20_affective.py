"""Finite exact arithmetic checks for MSC 97C20; not a formal proof assistant."""
from fractions import Fraction as F
from math import isclose, sqrt, exp
import unittest


def posterior(prior, sensitivity, false_positive):
    return sensitivity * prior / (sensitivity * prior + false_positive * (1-prior))


def transition(p, a, b):
    return (1-a-b)*p+b


class AffectiveMathematicsTests(unittest.TestCase):
    def test_weighted_mean(self):
        self.assertEqual((12*6+18*8)/30, 7.2)

    def test_ordinal_recoding(self):
        self.assertEqual((1+3)/2, 2)
        self.assertEqual((2+2)/2, 2)
        self.assertEqual((1+100)/2, 50.5)

    def test_total_probability(self):
        self.assertEqual(F(7,10)*F(8,10)+F(3,10)*F(2,10), F(31,50))

    def test_simpson_strata(self):
        self.assertGreater(F(9,10), F(80,100))
        self.assertGreater(F(20,100), F(1,10))
        self.assertLess(F(29,110), F(81,110))

    def test_randomization_inclusion_probability(self):
        self.assertEqual(F(10,40), F(1,4))

    def test_finite_population_effect(self):
        self.assertEqual(sum([2]*40)/40, 2)

    def test_measurement_attenuation(self):
        self.assertEqual(F(9,16), F(9,9+7))
        self.assertTrue(isclose(sqrt(9/16), .75))
        self.assertTrue(isclose(.8*sqrt(9/16), .6))

    def test_outcome_dependent_missingness(self):
        self.assertEqual(posterior(F(1,2), F(9,10), F(1,10)), F(9,10))

    def test_bayes_posterior(self):
        self.assertEqual(posterior(F(3,10), F(8,10), F(2,10)), F(12,19))

    def test_bayes_odds(self):
        post=posterior(F(3,10), F(8,10), F(2,10))
        self.assertEqual(post/(1-post), F(12,7))

    def test_markov_step(self):
        self.assertEqual(transition(F(2,5),F(1,5),F(3,10)), F(1,2))

    def test_markov_fixed_point(self):
        a,b=F(1,5),F(3,10)
        fixed=b/(a+b)
        self.assertEqual(fixed,F(3,5))
        self.assertEqual(transition(fixed,a,b),fixed)

    def test_markov_three_steps(self):
        p,a,b=F(2,5),F(1,5),F(3,10)
        for _ in range(3):p=transition(p,a,b)
        self.assertEqual(p,F(23,40))

    def test_logistic_symmetry(self):
        for x in [-3,-1,0,1,3]:
            sig=lambda t:1/(1+exp(-t))
            self.assertTrue(isclose(sig(-x),1-sig(x),rel_tol=1e-13))

    def test_bonferroni(self):
        self.assertEqual(F(5,100)/20,F(1,400))

    def test_bernoulli_variance(self):
        self.assertEqual(F(1,2)*F(1,2)/100,F(1,400))

    def test_chebyshev_bound(self):
        self.assertEqual(F(1,1)/(4*400*F(1,10)**2),F(1,16))

    def test_expectation_without_independence(self):
        self.assertEqual(F(4,10)+F(7,10)+F(9,10),2)

    def test_group_success_rates(self):
        self.assertEqual(F(12+27,60),F(13,20))
        self.assertEqual(F(12,24),F(1,2))
        self.assertEqual(F(27,36),F(3,4))

    def test_markov_convergence_exact(self):
        a,b=F(1,5),F(3,10)
        p0=F(2,5)
        fixed=b/(a+b)
        for t in range(10):
            p=p0
            for _ in range(t):p=transition(p,a,b)
            self.assertEqual(p-fixed,(1-a-b)**t*(p0-fixed))


if __name__=='__main__':unittest.main()
