"""Testy obliczeniowe przykładów z suplementu F11.2.

Nie są formalnym dowodem twierdzeń ogólnych. Uruchom:
python -m unittest discover -s tests -p test_f112.py -v
"""
from collections import Counter
from itertools import permutations, product
from pathlib import Path
import math
import random
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'manuscript/tom-01/F11/F11.2_UZUPELNIENIE_PRZEMIENNOSC.md'


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


class F112Verification(unittest.TestCase):
    def test_source_sections_and_exercises(self):
        s = SOURCE.read_text(encoding='utf-8')
        for i in range(1, 11):
            self.assertIn(f'**T{i} (', s)
        for i in range(1, 13):
            self.assertIn(f'**Z{i}.**', s)
        for i in range(1, 7):
            self.assertIn(f'**K{i} (', s)

    def test_t1_permutation_invariance(self):
        for n in range(7):
            xs = tuple(range(n))
            for p in permutations(xs):
                self.assertEqual(sum(xs), sum(p))

    def test_t2_local_commuting_matrices(self):
        i = ((1,0),(0,1))
        a = ((1,2),(3,4))
        b = ((2,4),(6,8))  # b=2a; commute
        self.assertEqual(matmul(a,b), matmul(b,a))
        self.assertEqual(matmul(matmul(i,a),b), matmul(matmul(b,a),i))

    def test_t3_center_contains_identity(self):
        i = ((1,0),(0,1))
        matrices = [((a,b),(c,d)) for a,b,c,d in product(range(-1,2), repeat=4)]
        for m in matrices:
            self.assertEqual(matmul(i,m), matmul(m,i))

    def test_t4_multiset_homomorphism(self):
        rng = random.Random(112)
        weights = {'a':2,'b':5,'c':7}
        for _ in range(300):
            m = Counter({k:rng.randrange(7) for k in weights})
            n = Counter({k:rng.randrange(7) for k in weights})
            f = lambda x: sum(weights[k]*v for k,v in x.items())
            self.assertEqual(f(m+n), f(m)+f(n))
        self.assertEqual(2*2+3*5, 19)

    def test_t5_partitions(self):
        xs = [2,4,7,1]
        self.assertEqual(sum(xs), sum(xs[i] for i in (0,2))+sum(xs[i] for i in (1,3)))
        self.assertEqual(sum(xs), 14)

    def test_t6_tag_swap_involution(self):
        a = {1,2}; b = {2,3}
        tagged = {(x,0) for x in a} | {(x,1) for x in b}
        tau = lambda x: (x[0],1-x[1])
        self.assertEqual({tau(tau(x)) for x in tagged}, tagged)
        self.assertEqual(len(tagged),4)

    def test_t7_disjoint_cardinality(self):
        for n in range(8):
            for m in range(8):
                a = set(range(n)); b = set(range(m))
                disjoint = {(x,0) for x in a} | {(x,1) for x in b}
                self.assertEqual(len(disjoint),n+m)

    def test_t8_multiset_cancellation(self):
        rng = random.Random(813)
        for _ in range(300):
            m = Counter({x:rng.randrange(6) for x in 'abc'})
            n = Counter({x:rng.randrange(6) for x in 'abc'})
            l = Counter({x:rng.randrange(6) for x in 'abc'})
            self.assertEqual(m+l==n+l,m==n)

    def test_t9_abelianization_word_count(self):
        # Dla wolnego monoidu słów abelianizacja zlicza wystąpienia liter.
        words = ['','a','b','ab','ba','abba','baab','aabb']
        for u in words:
            for v in words:
                self.assertEqual(Counter(u+v),Counter(v+u))
        self.assertEqual(Counter('abba'),Counter('baab'))

    def test_t10_fiber_grouping(self):
        rng = random.Random(999)
        for n in range(50):
            weights = [rng.randrange(100) for _ in range(n)]
            fibers = [rng.randrange(9) for _ in range(n)]
            self.assertEqual(sum(weights),sum(sum(weights[i] for i in range(n) if fibers[i]==j) for j in range(9)))

    def test_k1_commutative_not_associative(self):
        avg=lambda x,y:(x+y)/2
        self.assertEqual(avg(avg(0,2),4),2.5)
        self.assertEqual(avg(0,avg(2,4)),1.5)

    def test_k2_noncommutative_words(self):
        self.assertNotEqual('ab'+'ba','ba'+'ab')

    def test_k3_max_not_cancellative(self):
        self.assertEqual(max(0,2),max(1,2))
        self.assertNotEqual(0,1)

    def test_k5_binary64_rounding(self):
        self.assertEqual((1e16+(-1e16))+1.0,1.0)
        self.assertEqual(1e16+((-1e16)+1.0),0.0)

    def test_k6_matrix_noncommutativity(self):
        a=((1,1),(0,1)); b=((1,0),(1,1))
        self.assertEqual(matmul(a,b),((2,1),(1,1)))
        self.assertEqual(matmul(b,a),((1,1),(1,2)))


if __name__ == '__main__':
    unittest.main()
