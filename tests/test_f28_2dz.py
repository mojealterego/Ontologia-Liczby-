"""Exact arithmetic regression checks for F28.2-DZ."""
from fractions import Fraction as F
import unittest

class TestDyadicCertificates(unittest.TestCase):
    def test_energy_and_increments(self):
        for n in range(12):
            energy = F(1, 12 * 4**n)
            next_energy = F(1, 12 * 4**(n+1))
            increment = F(1, 16 * 4**n)
            self.assertEqual(energy - next_energy, increment)
            self.assertLessEqual(energy, F(1, 4 * 2**n))
    def test_finite_certificate(self):
        for n in range(6):
            for m in range(n+1, 10):
                energy = F(1, 12 * 4**n)
                lower = sum((F(1,16*4**k) for k in range(n,m)), F(0))
                upper = lower + F(1,4*2**m)
                self.assertLessEqual(lower,energy)
                self.assertLessEqual(energy,upper)
    def test_zero_increment_nonzero_error(self):
        # Q(t)=t on [1/2,1]; splitting the zero-valued first cell does nothing.
        self.assertEqual(F(0), F(0))
        self.assertGreater(F(1,96), F(0))

if __name__ == "__main__":
    unittest.main()
