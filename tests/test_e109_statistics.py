"""E1-09 descriptive statistics: exact regression and exhaustive finite checks."""
from fractions import Fraction as F
from itertools import product
import unittest

def mean(xs):
    if not xs:
        raise ValueError("empty sample")
    return sum(map(F,xs),F(0))/len(xs)

def variance(xs):
    mu=mean(xs)
    return sum(((F(x)-mu)**2 for x in xs),F(0))/len(xs)

def median(xs):
    if not xs:
        raise ValueError("empty sample")
    ys=sorted(map(F,xs))
    n=len(ys)
    return ys[n//2] if n%2 else (ys[n//2-1]+ys[n//2])/2

def quartiles_halves(xs):
    ys=sorted(map(F,xs))
    if len(ys)<4:
        raise ValueError("at least four observations")
    h=len(ys)//2
    return median(ys[:h]),median(ys[-h:])

class DescriptiveStatisticsTests(unittest.TestCase):
    def test_mean_in_range(self):
        for n in range(1,5):
            for xs in product(range(-2,3),repeat=n):
                self.assertLessEqual(min(xs),mean(xs))
                self.assertLessEqual(mean(xs),max(xs))

    def test_zero_sum_deviations(self):
        for xs in product(range(-2,3),repeat=3):
            mu=mean(xs)
            self.assertEqual(sum((F(x)-mu for x in xs),F(0)),0)

    def test_variance_identity(self):
        for xs in product(range(-2,3),repeat=3):
            self.assertEqual(variance(xs),mean([x*x for x in xs])-mean(xs)**2)

    def test_shift_scale(self):
        for xs in product(range(-2,3),repeat=3):
            self.assertEqual(mean([x+7 for x in xs]),mean(xs)+7)
            self.assertEqual(variance([x+7 for x in xs]),variance(xs))
            self.assertEqual(variance([3*x for x in xs]),9*variance(xs))

    def test_mean_minimizes_squared_loss(self):
        for xs in product(range(-2,3),repeat=3):
            mu=mean(xs)
            best=sum(((F(x)-mu)**2 for x in xs),F(0))
            for a in range(-4,5):
                self.assertGreaterEqual(sum(((F(x)-a)**2 for x in xs),F(0)),best)

    def test_median_minimizes_absolute_loss(self):
        for xs in product(range(-2,3),repeat=3):
            med=median(xs)
            best=sum((abs(F(x)-med) for x in xs),F(0))
            for a in range(-4,5):
                self.assertGreaterEqual(sum((abs(F(x)-a) for x in xs),F(0)),best)

    def test_pooled_mean(self):
        a=[1,3];b=[7,9,11]
        self.assertEqual(mean(a+b),F(len(a))*mean(a)/5+F(len(b))*mean(b)/5)

    def test_total_variance(self):
        a=[0,2];b=[4,6]
        mu=mean(a+b)
        pooled=(len(a)*(variance(a)+(mean(a)-mu)**2)+len(b)*(variance(b)+(mean(b)-mu)**2))/(len(a)+len(b))
        self.assertEqual(pooled,variance(a+b))
        self.assertEqual(pooled,5)

    def test_range_bound(self):
        for xs in product(range(4),repeat=4):
            self.assertLessEqual(variance(xs),F((max(xs)-min(xs))**2,4))

    def test_chebyshev(self):
        for xs in product(range(4),repeat=4):
            mu=mean(xs)
            for t in (F(1,2),F(1),F(2)):
                count=sum(abs(F(x)-mu)>=t for x in xs)
                self.assertLessEqual(F(count,len(xs)),variance(xs)/(t*t))

    def test_quartiles_explicit_convention(self):
        self.assertEqual(quartiles_halves([1,2,3,4,5]),(F(3,2),F(9,2)))
        self.assertEqual(quartiles_halves([1,2,3,4]),(F(3,2),F(7,2)))

    def test_weighted_mean(self):
        xs=[3,5];ws=[1,3]
        weighted=sum(F(x)*w for x,w in zip(xs,ws))/sum(ws)
        self.assertEqual(weighted,F(9,2))

    def test_singleton_sample_variance(self):
        self.assertEqual(variance([7]),0)
        with self.assertRaises(ZeroDivisionError):
            _=F(0,len([7])-1)

if __name__=="__main__":
    unittest.main()
