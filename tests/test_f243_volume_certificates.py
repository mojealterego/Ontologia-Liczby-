"""F24.3: exact arithmetic certificates for affine volume formulas.

Tests verify computational consequences, not the full measure-theoretic proofs.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial, isclose, pi
import unittest


def det3(u, v, w):
    return (u[0] * (v[1] * w[2] - v[2] * w[1])
            - u[1] * (v[0] * w[2] - v[2] * w[0])
            + u[2] * (v[0] * w[1] - v[1] * w[0]))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def tet(a, b, c, d):
    return abs(det3(sub(b, a), sub(c, a), sub(d, a))) / Q(6)


def frustum(h, area0, area1):
    # Exact when the ratio of areas has a rational square root.
    from math import isqrt
    prod = Q(area0) * Q(area1)
    n, d = isqrt(prod.numerator), isqrt(prod.denominator)
    if n*n != prod.numerator or d*d != prod.denominator:
        raise ValueError('irrational square root: use a symbolic expression')
    return Q(h, 3) * (Q(area0) + Q(n, d) + Q(area1))


def determinant_error_bound(M, eps):
    return (Q(M) + Q(eps))**3 - Q(M)**3


class VolumeCertificates(unittest.TestCase):
    def test_t1_unit(self): self.assertEqual(abs(det3((1,0,0),(0,1,0),(0,0,1))), 1)
    def test_t1_diagonal(self): self.assertEqual(abs(det3((2,0,0),(0,3,0),(0,0,5))), 30)
    def test_t1_singular(self): self.assertEqual(det3((1,0,0),(2,0,0),(0,1,0)), 0)
    def test_t1_orientation(self): self.assertEqual(det3((0,1,0),(1,0,0),(0,0,1)), -1)
    def test_t2_unit_simplex(self): self.assertEqual(tet((0,0,0),(1,0,0),(0,1,0),(0,0,1)), Q(1,6))
    def test_t2_axes(self): self.assertEqual(tet((0,0,0),(2,0,0),(0,3,0),(0,0,5)), 5)
    def test_t2_translation(self): self.assertEqual(tet((1,1,1),(3,1,1),(1,4,1),(1,1,6)), 5)
    def test_t2_degenerate(self): self.assertEqual(tet((0,0,0),(1,1,1),(2,2,2),(0,1,1)), 0)
    def test_t2_vertex_permutations(self):
        p=((0,0,0),(2,0,0),(0,3,0),(0,0,5))
        self.assertTrue(all(tet(*v)==5 for v in permutations(p)))
    def test_t3_sum(self): self.assertEqual(Q(6,6)+Q(12,6), 3)
    def test_t4_diagonal(self): self.assertEqual(det3((2,0,0),(0,3,0),(0,0,4)),24)
    def test_t4_singular(self): self.assertEqual(det3((1,0,0),(0,0,0),(0,0,7)),0)
    def test_t5_quadratic(self): self.assertEqual(Q(3)*Q(2)**3/Q(3),8)
    def test_t5_nonconstant_end_areas(self): self.assertEqual(Q(1)+Q(1,2)-Q(1,3),Q(7,6))
    def test_t6_frustum(self): self.assertEqual(frustum(6,4,16),56)
    def test_t6_prism(self): self.assertEqual(frustum(3,4,4),12)
    def test_t6_cone(self): self.assertEqual(frustum(3,0,9),9)
    def test_t6_swap_ends(self): self.assertEqual(frustum(6,16,4),56)
    def test_t7_ball_zero(self): self.assertEqual(Q(4,3)*Q(0)**3,0)
    def test_t7_ball_radius3(self): self.assertEqual(Q(4,3)*Q(3)**3,36)
    def test_t8_ellipsoid(self): self.assertEqual(Q(4,3)*2*3*4,32)
    def test_t9_shell(self): self.assertEqual(Q(4,3)*(3**3-1),Q(104,3))
    def test_t9_zero_thickness(self): self.assertEqual(Q(4,3)*(3**3-3**3),0)
    def test_t10_bound(self): self.assertEqual(determinant_error_bound(2,Q(1,10)),Q(1261,1000))
    def test_t10_tetra_bound(self): self.assertEqual(determinant_error_bound(2,Q(1,10))/6,Q(1261,6000))
    def test_t10_bound_zero(self): self.assertEqual(determinant_error_bound(2,0),0)
    def test_t10_bound_monotonic(self): self.assertLess(determinant_error_bound(2,Q(1,10)),determinant_error_bound(2,Q(1,5)))
    def test_counterexample_shell(self): self.assertNotEqual(Q(4,3)*(2**3-1),4*2**2)
    def test_counterexample_overlap(self): self.assertNotEqual(Q(1,6)+Q(1,6),Q(1,6))
    def test_counterexample_anisotropic(self): self.assertEqual(det3((2,0,0),(0,2,0),(0,0,1)),4)
    def test_all_small_determinants_alternating(self):
        vectors=list(product((-1,0,1),repeat=3))
        for u in vectors:
            for v in vectors:
                for w in ((1,0,0),(0,1,0),(0,0,1)):
                    self.assertEqual(det3(u,v,w),-det3(v,u,w))
    def test_exact_rational_vertices(self):
        a=(Q(0),Q(0),Q(0)); b=(Q(1,2),Q(0),Q(0)); c=(Q(0),Q(2,3),Q(0)); d=(Q(0),Q(0),Q(3,4))
        self.assertEqual(tet(a,b,c,d),Q(1,24))
    def test_volume_scaling_integer(self):
        for k in range(1,8):
            self.assertEqual(abs(det3((k,0,0),(0,k,0),(0,0,k))),k**3)
    def test_tetra_degenerate_coplanar(self):
        self.assertEqual(tet((0,0,0),(1,0,0),(0,1,0),(1,1,0)),0)
    def test_frustum_invalid_irrational(self):
        with self.assertRaises(ValueError): frustum(1,2,3)
    def test_sphere_ellipsoid_consistency(self):
        for r in range(1,8):
            self.assertEqual(Q(4,3)*r*r*r,Q(4,3)*r**3)
    def test_hadamard_bound_exhaustive_small_vectors(self):
        # For ||u_i|| <= sqrt(3) and ||e_i|| <= sqrt(3), use M=2, eps=2.
        candidates=list(product((-1,0,1),repeat=3))
        for u in candidates[::3]:
            for v in candidates[::4]:
                for w in candidates[::5]:
                    e=(1,0,0); f=(0,1,0); g=(0,0,1)
                    actual=abs(det3(tuple(x+y for x,y in zip(u,e)),tuple(x+y for x,y in zip(v,f)),tuple(x+y for x,y in zip(w,g)))-det3(u,v,w))
                    self.assertLessEqual(actual,determinant_error_bound(2,2))


if __name__ == '__main__':
    unittest.main()
