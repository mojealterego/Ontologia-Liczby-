"""F20.3: exact finite checks, not a proof of general theorems."""
import unittest
from fractions import Fraction as F
from itertools import product


def dim_add(a,b): return tuple(x+y for x,y in zip(a,b))
def dim_sub(a,b): return tuple(x-y for x,y in zip(a,b))
def convert(q,d,c):
    z=F(1)
    for e,base in zip(d,c): z*=base**e
    return q/z

def err_power(delta,n): return abs((1+delta)**n-1)
def bound(eta,n): return n*eta*(1+eta)**(n-1)

class Dimensions(unittest.TestCase):
    def test_dimensions_force(self): self.assertEqual(dim_add((0,1,0),(1,0,-2)),(1,1,-2))
    def test_dimensions_energy(self): self.assertEqual(dim_add((1,1,-2),(1,0,0)),(2,1,-2))
    def test_inverse_dimension(self): self.assertEqual(dim_sub((1,0,0),(0,0,1)),(1,0,-1))
    def test_unit_composition(self):
        for d in product(range(-2,3),repeat=3):
            a=(F(2),F(3),F(5)); b=(F(7),F(11),F(13)); q=F(37,19)
            self.assertEqual(convert(convert(q,d,a),d,b),convert(q,d,tuple(x*y for x,y in zip(a,b))))
    def test_product_conversion(self):
        for d,e in [((1,0,-1),(0,1,0)),((2,1,-2),(-1,0,2))]:
            c=(F(2),F(3),F(5))
            self.assertEqual(convert(F(6),dim_add(d,e),c),convert(F(2),d,c)*convert(F(3),e,c))
    def test_additive_conversion(self):
        d=(1,0,-1); c=(F(2),F(3),F(5))
        self.assertEqual(convert(F(2)+F(3),d,c),convert(F(2),d,c)+convert(F(3),d,c))
    def test_homothety_absolute(self): self.assertEqual(abs(F(-2))**3,F(8))
    def test_map_conversion(self): self.assertEqual(F(5,2)*40000,F(100000))
    def test_speed_conversion(self): self.assertEqual(F(90)*1000/3600,F(25))
    def test_power_exact(self): self.assertEqual(err_power(F(1,10),2),F(21,100))
    def test_power_negative(self): self.assertEqual(err_power(F(-1,20),3),F(1141,8000))
    def test_power_bound(self):
        for n in range(1,9):
            for delta in [F(i,100) for i in range(-30,31)]:
                self.assertLessEqual(err_power(delta,n),bound(abs(delta),n))
    def test_interval_positive(self):
        for n in range(1,8):
            for x in [F(2),F(5,2),F(3)]:
                self.assertTrue(F(2)**n<=x**n<=F(3)**n)
    def test_inverse_interval(self):
        for x in [F(2),F(5,2),F(3)]: self.assertTrue(F(1,9)<=x**-2<=F(1,4))
    def test_dimensionless(self):
        s=(1,0,0); v=(1,0,-1); a=(1,0,-2)
        self.assertEqual(dim_sub(dim_add(a,s),tuple(2*x for x in v)),(0,0,0))
    def test_affine_difference(self): self.assertEqual((2*15+10)-(2*5+10),2*(15-5))
    def test_affine_ratio_not_invariant(self): self.assertNotEqual(F(2*15+10,2*5+10),F(15,5))
    def test_dimension_failure(self): self.assertNotEqual((1,0,0),(0,0,1))
    def test_cube_factor(self): self.assertEqual(F(3,2)**3,F(27,8))
    def test_rounded_error_bound(self): self.assertEqual(bound(F(1,100),2),F(101,5000))

if __name__ == '__main__': unittest.main()
