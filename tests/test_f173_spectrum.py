"""Standard-library verification of the finite Dirichlet spectrum in F17.3."""
import math
import random
import unittest
from fractions import Fraction
from itertools import product


def laplacian(v):
    return [2 * v[i] - (v[i-1] if i else 0) - (v[i+1] if i+1 < len(v) else 0) for i in range(len(v))]


def dot(u, v):
    return sum(a*b for a,b in zip(u,v))


def mode(n, k):
    return [math.sin(math.pi*k*j/n) for j in range(1,n)]


def gap(n, k=1):
    return 2 - 2*math.cos(math.pi*k/n)


def green(n, i, j):
    return Fraction(min(i,j)*(n-max(i,j)), n)


def solve_exact(source):
    """Independent exact Gaussian elimination of the Dirichlet system."""
    m=len(source)
    A=[[Fraction(2 if i==j else (-1 if abs(i-j)==1 else 0)) for j in range(m)]+[Fraction(source[i])] for i in range(m)]
    for k in range(m):
        p=A[k][k]
        assert p!=0
        for j in range(k,m+1): A[k][j]/=p
        for i in range(k+1,m):
            q=A[i][k]
            for j in range(k,m+1): A[i][j]-=q*A[k][j]
    x=[Fraction(0)]*m
    for i in range(m-1,-1,-1): x[i]=A[i][m]-sum(A[i][j]*x[j] for j in range(i+1,m))
    return x


class TestSpectrum(unittest.TestCase):
    def test_eigenvectors(self):
        for n in range(2,35):
            for k in range(1,n):
                v=mode(n,k)
                self.assertLess(max(abs(a-gap(n,k)*b) for a,b in zip(laplacian(v),v)),1e-11)

    def test_ordered_positive_eigenvalues(self):
        for n in range(2,100):
            values=[gap(n,k) for k in range(1,n)]
            self.assertTrue(0<values[0] and values[-1]<4)
            self.assertTrue(all(a<b for a,b in zip(values,values[1:])))

    def test_orthogonality_and_norm(self):
        for n in range(2,28):
            modes=[mode(n,k) for k in range(1,n)]
            for k,v in enumerate(modes):
                self.assertAlmostEqual(dot(v,v),n/2,places=10)
                for u in modes[:k]: self.assertAlmostEqual(dot(u,v),0,places=10)

    def test_green_inverse_exact(self):
        for n in range(2,32):
            for j in range(1,n):
                column=[green(n,i,j) for i in range(1,n)]
                self.assertEqual(laplacian(column),[int(i==j) for i in range(1,n)])

    def test_green_spectral(self):
        for n in range(2,22):
            for i in range(1,n):
                for j in range(1,n):
                    result=sum((2/n)*math.sin(math.pi*k*i/n)*math.sin(math.pi*k*j/n)/gap(n,k) for k in range(1,n))
                    self.assertAlmostEqual(result,float(green(n,i,j)),places=9)

    def test_exact_poisson(self):
        for n in range(2,9):
            for values in product((-2,0,3),repeat=min(n-1,4)):
                f=tuple(values)+(0,)*max(0,n-5)
                expected=[sum(green(n,i,j)*f[j-1] for j in range(1,n)) for i in range(1,n)]
                self.assertEqual(solve_exact(f),expected)

    def test_sharp_poincare(self):
        for n in range(2,40):
            v=mode(n,1)
            self.assertAlmostEqual(dot(v,laplacian(v)),gap(n)*dot(v,v),places=10)
            rng=random.Random(n)
            for _ in range(25):
                x=[rng.randint(-9,9) for i in range(n-1)]
                self.assertGreaterEqual(dot(x,laplacian(x))+1e-9,gap(n)*dot(x,x))

    def test_operator_bound(self):
        for n in range(2,18):
            f=[Fraction((i*7+n)%11-5) for i in range(n-1)]
            v=solve_exact(f)
            self.assertLessEqual(float(dot(v,v)),float(dot(f,f))/gap(n)**2+1e-8)

    def test_heat_decay(self):
        for n in range(2,30):
            x=[float(j) for j in range(1,n)]
            modes=[mode(n,k) for k in range(1,n)]
            coeffs=[2/n*dot(x,v) for v in modes]
            for t in (0,0.1,1,3):
                v=[sum(coeffs[k-1]*math.exp(-gap(n,k)*t)*modes[k-1][j] for k in range(1,n)) for j in range(n-1)]
                self.assertLessEqual(dot(v,v),math.exp(-2*gap(n)*t)*dot(x,x)+1e-8)

    def test_empty_interior(self):
        self.assertEqual([],mode(1,1))
        self.assertEqual([],laplacian([]))

if __name__=='__main__': unittest.main()
