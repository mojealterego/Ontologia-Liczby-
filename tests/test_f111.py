"""Kontrole skończonych przypadków F11.1; nie są dowodami twierdzeń ogólnych."""
import itertools
import unittest


def iterate_mod(n, x, mod):
    a = 0
    for _ in range(n):
        a = (a + x) % mod
    return a


def is_leq(a, b):
    return any(a + c == b for c in range(b + 1))


class TestF111(unittest.TestCase):
    def test_iteration_additivity(self):
        for mod in range(2, 12):
            for x in range(mod):
                for m in range(15):
                    for n in range(15):
                        self.assertEqual(iterate_mod(m+n, x, mod),
                                         (iterate_mod(m,x,mod)+iterate_mod(n,x,mod))%mod)

    def test_iteration_uniqueness_recurrence(self):
        for mod in range(2, 10):
            for x in range(mod):
                values = [0]
                for _ in range(30):
                    values.append((values[-1] + x) % mod)
                self.assertEqual(values, [iterate_mod(n,x,mod) for n in range(31)])

    def test_noncommutative_cyclic_submonoid(self):
        for x in ('a', 'ab', 'xy'):
            for m in range(8):
                for n in range(8):
                    self.assertEqual(x*m+x*n, x*(m+n))
                    self.assertEqual(x*m+x*n, x*n+x*m)

    def test_endomorphisms(self):
        for k in range(15):
            for a in range(20):
                for b in range(20):
                    self.assertEqual(k*(a+b),k*a+k*b)

    def test_permutation_invariance(self):
        for n in range(7):
            values = tuple(range(n))
            expected = sum(values)
            for permutation in itertools.permutations(values):
                self.assertEqual(sum(permutation), expected)

    def test_disjoint_partition(self):
        values = (2,0,5,3)
        for mask in range(1 << len(values)):
            left = sum(x for i,x in enumerate(values) if mask & (1 << i))
            right = sum(x for i,x in enumerate(values) if not mask & (1 << i))
            self.assertEqual(left+right, sum(values))

    def test_natural_difference_unique(self):
        for a in range(50):
            for b in range(50):
                solutions = [c for c in range(50) if a+c == b]
                self.assertEqual(len(solutions), int(a <= b))
                if solutions:
                    self.assertEqual(solutions[0], b-a)

    def test_translation_of_order(self):
        for a in range(15):
            for b in range(15):
                for t in range(15):
                    self.assertEqual(is_leq(a,b), is_leq(a+t,b+t))
                    self.assertEqual(a < b, a+t < b+t)

    def test_no_positive_inverse(self):
        for a in range(50):
            for b in range(50):
                self.assertEqual(a+b==0, a==b==0)

    def test_cyclic_order(self):
        for mod in range(2, 20):
            for g in range(mod):
                order = next(r for r in range(1,mod+1) if (r*g)%mod == 0)
                for n in range(80):
                    self.assertEqual((n*g)%mod == 0, n%order==0)
                    self.assertEqual(((n+order)*g)%mod,(n*g)%mod)

    def test_counterexamples(self):
        self.assertEqual(max(0,2),max(1,2))
        self.assertNotEqual(0,1)
        self.assertNotEqual('ab'+'c','c'+'ab')
        self.assertNotEqual((1+1)**2,1**2+1**2)
        self.assertEqual(0%3,3%3)
        self.assertFalse(any(7+c==4 for c in range(20)))

    def test_exercises(self):
        self.assertEqual(7*3%5,(4*3+3*3)%5)
        self.assertEqual(3*4,12)
        self.assertFalse(any(3*k==10 for k in range(20)))
        self.assertEqual(2+0+5+3,10)
        self.assertEqual(8+9,17)
        self.assertEqual(6+5,11)
        self.assertEqual(20+5,25)
        self.assertEqual(6*1+6*2,18)


if __name__ == '__main__':
    unittest.main()
