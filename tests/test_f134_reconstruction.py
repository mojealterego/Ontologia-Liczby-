import itertools
import math
import unittest
from fractions import Fraction

def factorial_moment(a,r):
    return sum(math.factorial(i)//math.factorial(i-r)*x for i,x in enumerate(a) if i>=r)

def reconstruct(moments):
    n=len(moments)-1
    out=[Fraction(0)]*(n+1)
    for r in range(n,-1,-1):
        higher=sum(math.factorial(i)//math.factorial(i-r)*out[i] for i in range(r+1,n+1))
        out[r]=(moments[r]-higher)/math.factorial(r)
    return out

class TestReconstruction(unittest.TestCase):
    def test_exhaustive(self):
        cases=0
        for length in range(1,6):
            for a in itertools.product((-2,-1,0,1,2),repeat=length):
                m=[factorial_moment(a,r) for r in range(length)]
                self.assertEqual(reconstruct(m),list(a))
                cases+=1
        self.assertEqual(cases,3905)
    def test_examples(self):
        self.assertEqual(reconstruct([9,11,8]),[2,3,4])
        self.assertEqual(reconstruct([3,-2]),[5,-2])
    def test_ambiguity_short_moments(self):
        self.assertEqual([factorial_moment([0,0,0],r) for r in range(2)], [factorial_moment([1,-2,1],r) for r in range(2)])

if __name__=="__main__":
    unittest.main()
