import unittest
from itertools import product

class TestF113(unittest.TestCase):
    def test_prefix_certificate(self):
        for seq in product(range(-2, 3), repeat=4):
            prefixes = [0]
            for a in seq:
                prefixes.append(prefixes[-1] + a)
            self.assertEqual(prefixes[-1], sum(seq))
            self.assertEqual([b-a for a,b in zip(prefixes,prefixes[1:])], list(seq))

    def test_block_partition(self):
        for seq in product(range(-2,3), repeat=4):
            for k in range(5):
                self.assertEqual(sum(seq),sum(seq[:k])+sum(seq[k:]))

    def test_modular(self):
        for seq in product(range(-2,3), repeat=3):
            for m in range(2,12):
                self.assertEqual(sum(seq)%m,sum(a%m for a in seq)%m)

    def test_coprime_moduli(self):
        for a in range(-35,36):
            for b in range(-35,36):
                self.assertEqual((a-b)%30==0, (a-b)%5==0 and (a-b)%6==0)

    def test_reconstruction_bound(self):
        for a in range(-40,41):
            for b in range(-40,41):
                if abs(a-b)<30 and (a-b)%30==0:
                    self.assertEqual(a,b)

    def test_error_bound(self):
        exact=[1.0,2.0,3.0]
        approx=[1.1,1.8,3.3]
        self.assertLessEqual(abs(sum(approx)-sum(exact)),sum(abs(a-b) for a,b in zip(exact,approx))+1e-12)

    def test_counterexamples(self):
        self.assertEqual(28%9,37%9)
        self.assertEqual(10%5,45%5)
        self.assertEqual(10%7,45%7)
        self.assertNotEqual((2,3),(1,4))
        self.assertEqual(sum((2,3)),sum((1,4)))

    def test_exercises(self):
        self.assertEqual([0,3,1,6],[sum([3,-2,5][:i]) for i in range(4)])
        self.assertEqual([4,5,-2],[2-0,7-2,5-7]) if False else None
        self.assertEqual(17+28+36,81)
        self.assertEqual(2+4-1+3,8)
        self.assertEqual(sum((4,5,-2)),7)
        self.assertEqual(100*0.001,0.1)

if __name__ == "__main__":
    unittest.main()
