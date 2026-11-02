import math
import unittest

def moment(a, r):
    return sum(i**r*x for i,x in enumerate(a))

class HigherMoments(unittest.TestCase):
    def test_zero_moments(self):
        for s in range(9):
            d=[(-1)**i*math.comb(s+1,i) for i in range(s+2)]
            for r in range(s+1):
                self.assertEqual(moment(d,r),0)

    def test_example(self):
        self.assertEqual(moment([3,10,8],3),74)

if __name__ == "__main__":
    unittest.main()
