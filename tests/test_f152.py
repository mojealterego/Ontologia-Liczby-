import math
import random
import unittest


def extended_gcd(a: int, b: int):
    if a == 0 and b == 0:
        return 0, 0, 0, []
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    trace = []
    while r:
        q, rem = divmod(old_r, r)
        trace.append((old_r, r, q, rem))
        old_r, r = r, rem
        old_s, s = s, old_s - q*s
        old_t, t = t, old_t - q*t
    return old_r, old_s * (-1 if a < 0 else 1), old_t * (-1 if b < 0 else 1), trace


class TestF152(unittest.TestCase):
    def test_signed_euclidean_division(self):
        for a in range(-75, 76):
            for b in range(-15, 16):
                if not b:
                    continue
                d = abs(b)
                q0, r = divmod(a, d)
                q = q0 if b > 0 else -q0
                self.assertEqual(a, q*b+r)
                self.assertTrue(0 <= r < d)

    def test_bezout_exhaustive(self):
        for a in range(-50, 51):
            for b in range(-50, 51):
                g,u,v,_ = extended_gcd(a,b)
                self.assertEqual(g, math.gcd(a,b))
                self.assertEqual(a*u+b*v,g)
                if g:
                    self.assertEqual(a%g,0)
                    self.assertEqual(b%g,0)
                else:
                    self.assertEqual((a,b),(0,0))

    def test_trace(self):
        for a in range(1,100):
            for b in range(1,a+1):
                g,_,_,trace=extended_gcd(a,b)
                for x,y,q,r in trace:
                    self.assertEqual(x,q*y+r)
                    self.assertTrue(0<=r<y)
                self.assertEqual(trace[-1][-1],0)
                self.assertEqual(trace[-1][1],g)

    def test_two_step_halving(self):
        for a in range(1,200):
            for b in range(1,a+1):
                _,_,_,trace=extended_gcd(a,b)
                rs=[a,b]+[step[-1] for step in trace]
                for i in range(len(rs)-2):
                    if rs[i+2]>0 and i>=1:
                        self.assertLess(2*rs[i+2],rs[i])

    def test_modular_inverse(self):
        for m in range(2,60):
            for a in range(-60,61):
                g,u,_,_=extended_gcd(a,m)
                if g==1:
                    self.assertEqual((a*u)%m,1)
                else:
                    self.assertFalse(any((a*x)%m==1 for x in range(m)))

    def test_diophantine(self):
        for a in range(-15,16):
            for b in range(-15,16):
                g,u,v,_=extended_gcd(a,b)
                for c in (-6,-3,0,4,9):
                    if g and c%g==0:
                        k=c//g
                        self.assertEqual(a*(u*k)+b*(v*k),c)
                    elif g==0:
                        self.assertEqual(c==0, a==0 and b==0 and c==0)

    def test_example_1071(self):
        self.assertEqual(1071*(-3)+462*7,21)
        self.assertEqual(math.gcd(1071,462),21)

    def test_example_inverse(self):
        self.assertEqual((17*38)%43,1)

    def test_example_equation(self):
        self.assertEqual(15*3+21*(-2),3)

    def test_general_solution(self):
        for k in range(-100,101):
            self.assertEqual(6*(2+5*k)+10*(-1-3*k),2)

    def test_empty_case(self):
        self.assertEqual(extended_gcd(0,0)[:3],(0,0,0))

    def test_coefficient_determinants(self):
        for a in range(1,90):
            for b in range(1,a+1):
                old_r, r = a,b
                old_s,s = 1,0
                old_t,t = 0,1
                i=0
                while r:
                    self.assertEqual(old_s*t-s*old_t,(-1)**i)
                    self.assertEqual(old_r,old_s*a+old_t*b)
                    self.assertEqual(r,s*a+t*b)
                    q,rem=divmod(old_r,r)
                    old_r,r=r,rem
                    old_s,s=s,old_s-q*s
                    old_t,t=t,old_t-q*t
                    i+=1

    def test_logarithmic_bound(self):
        for a in range(1,250):
            for b in range(1,a+1):
                _,_,_,trace=extended_gcd(a,b)
                self.assertLessEqual(len(trace), 2*math.ceil(math.log2(b))+3)

    def test_random_large(self):
        rng=random.Random(20261030)
        for _ in range(250):
            a=rng.randrange(-10**50,10**50)
            b=rng.randrange(-10**50,10**50)
            g,u,v,_=extended_gcd(a,b)
            self.assertEqual(g,math.gcd(a,b))
            self.assertEqual(a*u+b*v,g)

if __name__ == '__main__':
    unittest.main()
