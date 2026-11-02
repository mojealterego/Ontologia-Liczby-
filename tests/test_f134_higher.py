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

    def test_binomial(self):
        for a in ([1,2], [1,-1,3], [0,2,0]):
            for b in ([2,4], [1,0,-1]):
                product=[sum(a[i]*b[k-i] for i in range(len(a)) if 0<=k-i<len(b)) for k in range(len(a)+len(b)-1)]
                for r in range(5):
                    expected=sum(math.comb(r,j)*moment(a,j)*moment(b,r-j) for j in range(r+1))
                    self.assertEqual(moment(product,r),expected)

    def test_vandermonde_boundary(self):
        for n in range(1,9):
            d=[(-1)**i*math.comb(n,i) for i in range(n+1)]
            self.assertEqual([moment(d,r) for r in range(n)],[0]*n)
            self.assertNotEqual(moment(d,n),0)

    def test_example(self):
        self.assertEqual(moment([3,10,8],3),74)

if __name__ == "__main__":
    unittest.main()
