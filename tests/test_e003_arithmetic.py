"""E0-03: arithmetic invariants, standard-library executable tests."""
import unittest

class ArithmeticE003(unittest.TestCase):
    def test_division_reconstruction(self):
        for a in range(100):
            for b in range(1, 31):
                q, r = divmod(a, b)
                self.assertEqual(a, b*q+r)
                self.assertLess(r, b)
                self.assertGreaterEqual(r, 0)

    def test_division_uniqueness(self):
        for a in range(100):
            for b in range(1, 20):
                pairs = [(q, r) for q in range(a+1) for r in range(b) if a == b*q+r]
                self.assertEqual(pairs, [divmod(a,b)])

    def test_distributivity(self):
        for a in range(20):
            for b in range(20):
                for c in range(10):
                    self.assertEqual(a*(b+c), a*b+a*c)

    def test_addition_carry_invariant(self):
        for a in range(0, 500, 7):
            for b in range(0, 500, 11):
                x, y = a, b
                carry = 0
                digits = 0
                prefix = 0
                power = 1
                while x or y:
                    dx, dy = x%10, y%10
                    t = dx+dy+carry
                    digit, carry = t%10, t//10
                    digits += digit*power
                    prefix += (dx+dy)*power
                    power *= 10
                    self.assertEqual(prefix, digits+carry*power)
                    x //= 10
                    y //= 10
                self.assertEqual(a+b, digits+carry*power)

    def test_parity(self):
        for a in range(100):
            for b in range(100):
                self.assertEqual((a*b)%2 == 1, a%2 == 1 and b%2 == 1)
                if a%2 and b%2:
                    self.assertEqual((a+b)%2, 0)

    def test_examples(self):
        self.assertEqual(487+568, 1055)
        self.assertEqual(137//12, 11)
        self.assertEqual(137%12, 5)
        self.assertEqual(48*25, 1200)
        self.assertEqual(17//5, 3)
        self.assertEqual(17%5, 2)

if __name__ == "__main__":
    unittest.main()
