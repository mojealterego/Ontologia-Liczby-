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


    def test_generalized_crt_three_moduli(self):
        for m in range(1, 7):
            for n in range(1, 7):
                for p in range(1, 7):
                    period = math.lcm(m, n, p)
                    for r in range(m):
                        for s in range(n):
                            for t in range(p):
                                compatible = ((s-r) % math.gcd(m, n) == 0
                                              and (t-r) % math.gcd(m, p) == 0
                                              and (t-s) % math.gcd(n, p) == 0)
                                found = any(x % m == r and x % n == s and x % p == t
                                            for x in range(period))
                                self.assertEqual(found, compatible)

    def test_constructive_crt(self):
        for m in range(1, 21):
            for n in range(1, 21):
                g = math.gcd(m, n)
                for r in range(m):
                    for s in range(n):
                        if (s-r) % g:
                            continue
                        mp, np = m//g, n//g
                        t = 0 if np == 1 else ((s-r)//g * pow(mp, -1, np)) % np
                        x = r + m*t
                        self.assertEqual(x % m, r)
                        self.assertEqual(x % n, s)
                        self.assertEqual(math.lcm(m,n), m*np)

    def test_first_nonnegative_index_meeting(self):
        for m in range(1, 11):
            for n in range(1, 11):
                for r in range(-3, 4):
                    for s in range(-3, 4):
                        g, period = math.gcd(m,n), math.lcm(m,n)
                        M = max(r,s)
                        hits = [x for x in range(M, M+period)
                                if (x-r)%m == 0 and (x-s)%n == 0]
                        self.assertEqual(len(hits), int((s-r)%g == 0))
                        if hits:
                            self.assertTrue(M <= hits[0] < M+period)
                            self.assertGreaterEqual((hits[0]-r)//m, 0)
                            self.assertGreaterEqual((hits[0]-s)//n, 0)

    def test_counting_formula(self):
        for m in range(1, 13):
            for n in range(1, 13):
                period = math.lcm(m,n)
                for x0 in range(period):
                    for T in (0, 1, period, period+1, 2*period+3):
                        actual = sum(x%period == x0 for x in range(T))
                        formula = 0 if T <= x0 else 1+(T-1-x0)//period
                        self.assertEqual(actual, formula)
                        self.assertLess(abs(actual-T/period), 1.0000001)

    def test_adjacent_pairs_not_sufficient(self):
        self.assertTrue(any(x%4==0 and x%5==0 for x in range(20)))
        self.assertTrue(any(x%5==0 and x%6==1 for x in range(30)))
        self.assertFalse(any(x%4==0 and x%6==1 for x in range(12)))

if __name__=="__main__":
    unittest.main()
