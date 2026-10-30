"""Reproducible finite checks for the F9.3 manuscript; not a proof of all theorems."""
import itertools
import math
import unittest
from pathlib import Path

SOURCE = Path(__file__).with_name('F9.3_UZUPELNIENIE_ODLICZANIE_A_DOWOD.md')

class F93Checks(unittest.TestCase):
    def test_manuscript_structure(self):
        text = SOURCE.read_text(encoding='utf-8')
        for i in range(1, 11):
            self.assertIn(f'Twierdzenie {i} (', text)
        for i in range(1, 13):
            self.assertIn(f'Zadanie {i}.', text)
        self.assertIn('**Status redakcyjny.**', text)
        self.assertIn('**Kontrprzykład 5', text)

    def test_euler_counterexample(self):
        p = lambda n: n*n+n+41
        self.assertEqual(p(40), 41*41)
        self.assertEqual(p(40), 1681)

    def test_finite_sample_poly(self):
        for k in range(8):
            S = list(range(k))
            g = lambda x: math.prod(x-s for s in S)
            for x in S:
                self.assertEqual(g(x), 0)
            self.assertNotEqual(g(k), 0)

    def test_degree_bound_for_polynomials(self):
        # Two degree-3 polynomials with identical values at 4 distinct points.
        f = lambda x: x**3-2*x+4
        g = lambda x: 4-2*x+x**3
        for x in range(-5, 6):
            self.assertEqual(f(x), g(x))
        # A degree-4 perturbation may match at four points but differ at a fifth.
        h = lambda x: f(x)+x*(x-1)*(x-2)*(x-3)
        for x in range(4):
            self.assertEqual(f(x), h(x))
        self.assertNotEqual(f(4), h(4))

    def test_equivalence_class_cardinality(self):
        U = [0,1,2,3]
        classes = [{0,1}, {2}, {3}]
        self.assertEqual(len(U), 4)
        self.assertEqual(len(classes), 3)
        self.assertEqual(set().union(*classes), set(U))
        for i, c in enumerate(classes):
            for d in classes[i+1:]:
                self.assertFalse(c & d)

    def test_finite_isomorphism_preserves_distinctness_sentence(self):
        for n in range(1, 6):
            A = list(range(n))
            for perm in itertools.permutations(A):
                self.assertEqual(len(set(perm)) == len(perm), True)
                self.assertEqual(n >= 2, len(set(perm)) >= 2)

    def test_surjection_does_not_preserve_distinctness(self):
        A = [0, 1]
        B = [0]
        mapping = {0:0,1:0}
        self.assertEqual(set(mapping.values()), set(B))
        self.assertEqual(len(A) >= 2, True)
        self.assertEqual(len(B) >= 2, False)

    def test_recursive_addition(self):
        def add(a,b):
            if b == 0: return a
            return add(a,b-1)+1
        for a in range(12):
            for b in range(12):
                self.assertEqual(add(a,b),a+b)
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(3,2),5)

    def test_evenness(self):
        for n in range(500):
            self.assertEqual((n*n+n)%2,0)

    def test_prime_counterexample(self):
        self.assertEqual(2**3+1,9)
        self.assertEqual(9%3,0)

    def test_powers_positive_reals(self):
        for x in [-100,-3,-1,0,1,3,100]:
            self.assertGreater(x*x+1,0)

    def test_empty_theory_countermodel(self):
        domain = {0}
        P = set()
        self.assertTrue(domain)
        self.assertFalse(all(x in P for x in domain))

if __name__ == '__main__':
    unittest.main()
