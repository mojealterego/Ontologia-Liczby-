"""F17.2: skończone testy arytmetyki, nie formalizacja dowodów."""
import itertools
import math
import unittest

def equal(p,q):
    a,b=p; c,d=q
    return a+d==b+c

def product(p,q):
    a,b=p; c,d=q
    return ac_bd(a,b,c,d)

def ac_bd(a,b,c,d):
    return (a*c+b*d,a*d+b*c)

def bezout(a,b):
    r0,r1=abs(a),abs(b)
    s0,s1=1,0
    t0,t1=0,1
    while r1:
        q=r0//r1
        r0,r1=r1,r0-q*r1
        s0,s1=s1,s0-q*s1
        t0,t1=t1,t0-q*t1
    return r0,s0*(1 if a>=0 else -1),t0*(1 if b>=0 else -1)

class TestF172(unittest.TestCase):
    def test_pair_equivalence(self):
        for a,b,c,d in itertools.product(range(7),repeat=4):
            self.assertEqual(equal((a,b),(c,d)),a-b==c-d)

    def test_pair_product(self):
        for a,b,c,d in itertools.product(range(6),repeat=4):
            x,y=product((a,b),(c,d))
            self.assertEqual(x-y,(a-b)*(c-d))

    def test_representative_independence(self):
        for a,b,c,d,k,l in itertools.product(range(3),repeat=6):
            self.assertTrue(equal(product((a,b),(c,d)),product((a+k,b+k),(c+l,d+l))))

    def test_distributivity(self):
        for a,b,c in itertools.product(range(-12,13),repeat=3):
            self.assertEqual(a*(b+c),a*b+a*c)

    def test_euclidean_division(self):
        for a in range(-150,151):
            for m in range(-21,22):
                if m==0: continue
                q,r=divmod(a,abs(m))
                if m<0: q=-q
                self.assertEqual(a,m*q+r)
                self.assertTrue(0<=r<abs(m))

    def test_bezout(self):
        for a in range(-35,36):
            for b in range(-35,36):
                if not(a or b):continue
                d,u,v=bezout(a,b)
                self.assertEqual(d,math.gcd(a,b))
                self.assertEqual(a*u+b*v,d)

    def test_linear_diophantine(self):
        for a,b,c in itertools.product(range(-8,9),repeat=3):
            if a==b==0:continue
            d=math.gcd(a,b)
            if c%d==0:
                g,u,v=bezout(a,b)
                self.assertEqual(a*u*(c//g)+b*v*(c//g),c)

    def test_modular_inverse(self):
        for m in range(2,70):
            for a in range(m):
                exists=any(a*x%m==1 for x in range(m))
                self.assertEqual(exists,math.gcd(a,m)==1)

    def test_congruence_count(self):
        for m in range(1,31):
            for a in range(-25,26):
                for b in range(-5,6):
                    count=sum((a*x-b)%m==0 for x in range(m))
                    d=math.gcd(a,m)
                    self.assertEqual(count,d if b%d==0 else 0)

    def test_reverse_triangle(self):
        for x,y in itertools.product(range(-40,41),repeat=2):
            self.assertLessEqual(abs(abs(x)-abs(y)),abs(x-y))

    def test_signs(self):
        for x,y in itertools.product(range(-50,51),repeat=2):
            if x and y:
                self.assertEqual(x*y>0,(x>0)==(y>0))

    def test_solved_examples(self):
        self.assertEqual(product((2,7),(9,4)),(46,71))
        self.assertEqual(bezout(414,276),(138,1,-1))
        self.assertEqual([x for x in range(9) if (6*x-3)%9==0],[2,5,8])
        self.assertEqual([x for x in range(9) if (6*x-4)%9==0],[])

if __name__=="__main__":
    unittest.main()
