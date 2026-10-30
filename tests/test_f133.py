"""Exhaustive and property tests for F13.3 schoolbook multiplication."""
import importlib.util
import random
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("long_multiply", ROOT / "tools" / "long_multiply.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Missing implementation module")
mod = importlib.util.module_from_spec(SPEC)
import sys
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class SchoolbookMultiplicationTests(unittest.TestCase):
    def test_zero(self):
        for b in (2,3,10,16,60):
            for x in range(45):
                self.assertEqual(mod.schoolbook_product(0,x,b).value,0)
                self.assertEqual(mod.schoolbook_product(x,0,b).value,0)

    def test_small_exhaustive(self):
        for b in range(2,13):
            for x in range(30):
                for y in range(30):
                    p=mod.schoolbook_product(x,y,b)
                    self.assertEqual(p.value,x*y)
                    self.assertEqual(p.reconstructed(),x*y)

    def test_trace_length(self):
        for b in (2,3,7,10,16,60):
            for x in range(1,100):
                for y in range(1,35):
                    p=mod.schoolbook_product(x,y,b)
                    self.assertLessEqual(len(p.digits),len(mod.digits_lsb(x,b))+len(mod.digits_lsb(y,b)))
                    self.assertTrue(all(0<=z<b for z in p.digits))

    def test_carry_recurrence(self):
        for b in (2,9,10,60):
            for x in (0,1,2,34,997,4096,123456):
                for y in (0,2,3,77,10203):
                    p=mod.schoolbook_product(x,y,b)
                    for k,digit in enumerate(p.digits):
                        self.assertEqual(p.coefficients[k]+p.carries[k],digit+b*p.carries[k+1])
                    self.assertEqual(p.carries[0],0)
                    self.assertEqual(p.carries[-1],0)

    def test_raw_convolution_identity(self):
        for b in (2,3,7,10,16,60):
            for a in (0,1,11,234,12345):
                for c in (0,1,31,987):
                    p=mod.schoolbook_product(a,c,b)
                    self.assertEqual(sum(z*b**i for i,z in enumerate(p.coefficients)),a*c)

    def test_signed(self):
        for b in (2,10,16):
            for x in (-450,-1,0,5,43):
                for y in (-97,-5,0,1,612):
                    self.assertEqual(mod.signed_product(x,y,b),x*y)

    def test_validation(self):
        for bad in (0,1,-2,True,2.1,"3"):
            with self.assertRaises((TypeError,ValueError)):
                mod.schoolbook_product(4,7,bad)
        for bad in (True,2.2,"5",-1):
            with self.assertRaises((TypeError,ValueError)):
                mod.schoolbook_product(bad,7,10)

    def test_random_large(self):
        rng=random.Random(20261030)
        for _ in range(250):
            b=rng.randint(2,80)
            x=rng.getrandbits(rng.randint(0,256))
            y=rng.getrandbits(rng.randint(0,256))
            self.assertEqual(mod.schoolbook_product(x,y,b).value,x*y)

    def test_decimal_example_from_manuscript(self):
        p=mod.schoolbook_product(247,36,10)
        self.assertEqual(p.value,8892)
        self.assertEqual(p.digits,(2,9,8,8))

    def test_base16_example(self):
        p=mod.schoolbook_product(0xA7,0x3D,16)
        self.assertEqual(p.value,0x27CB)

    def test_fixed_word_overflow(self):
        self.assertEqual(mod.fixed_word_product(999,999,10,3),(1,True))
        self.assertEqual(mod.fixed_word_product(99,1,10,3),(99,False))
        self.assertEqual(mod.fixed_word_product(2**16-1,2**16-1,2,16),(1,True))

    def test_karatsuba_identity(self):
        for x in range(31):
            for y in range(31):
                for m in (1,2):
                    high,low=divmod(x,10**m)
                    high2,low2=divmod(y,10**m)
                    z0=low*low2
                    z2=high*high2
                    z1=(high+low)*(high2+low2)-z0-z2
                    self.assertEqual(z2*10**(2*m)+z1*10**m+z0,x*y)

    def test_encoding_roundtrip(self):
        for b in (2,3,7,10,16,60):
            for x in range(1000):
                ds=mod.digits_lsb(x,b)
                self.assertEqual(sum(d*b**i for i,d in enumerate(ds)),x)
                self.assertTrue(all(0<=d<b for d in ds))

    def test_error_bound_modulo(self):
        for a in (0,1,1234,98765):
            for c in (0,1,9,987):
                p=mod.schoolbook_product(a,c,10)
                for q in (9,11,97):
                    self.assertEqual(p.value%q,(a%q)*(c%q)%q)


if __name__ == '__main__':
    unittest.main()
