import math
import unittest

class TestF153(unittest.TestCase):
    def test_crt_criterion(self):
        for m in range(1,13):
            for n in range(1,13):
                for r in range(m):
                    for s in range(n):
                        found=any(x%m==r and x%n==s for x in range(math.lcm(m,n)))
                        self.assertEqual(found,(s-r)%math.gcd(m,n)==0)

    def test_crt_count(self):
        for m in range(1,10):
            for n in range(1,10):
                count=sum(x%m==0 and x%n==0 for x in range(m*n))
                self.assertEqual(count,math.gcd(m,n))

    def test_linear_congruence(self):
        for m in range(1,20):
            for a in range(-12,13):
                for b in range(-12,13):
                    count=sum((a*x-b)%m==0 for x in range(m))
                    self.assertEqual(count,math.gcd(a,m) if b%math.gcd(a,m)==0 else 0)

    def test_periods(self):
        for m in range(1,25):
            for n in range(1,25):
                l=math.lcm(m,n)
                self.assertEqual([x for x in range(3*l) if x%m==0 and x%n==0],[0,l,2*l])

    def test_exercises(self):
        self.assertEqual([x for x in range(12) if x%4==1 and x%6==3],[9])
        self.assertEqual([x for x in range(9) if (6*x-3)%9==0],[2,5,8])
        self.assertEqual([x for x in range(12) if (4*x-8)%12==0],[2,5,8,11])
        self.assertEqual(math.lcm(3,4,10),60)
        self.assertEqual(math.gcd(84,126),42)
        self.assertEqual([x for x in range(30) if x%10==0 and x%15==5],[20])

if __name__=="__main__":
    unittest.main()
