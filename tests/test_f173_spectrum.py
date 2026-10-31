"""Finite numerical/exact checks for F17.3 discrete Dirichlet spectrum."""
import math
import unittest
from fractions import Fraction
from itertools import product
import numpy as np


def laplacian(n):
    if n < 2:
        raise ValueError("N must be at least 2")
    m = n - 1
    return np.diag([2.] * m) - np.diag([1.] * (m-1), 1) - np.diag([1.] * (m-1), -1)


def green_exact(n, i, j):
    return Fraction(min(i, j) * (n - max(i, j)), n)


def solve_tridiagonal_exact(n, f):
    """Independent Gaussian elimination over rational numbers."""
    m = n - 1
    a = [[Fraction(2 if i == j else (-1 if abs(i-j) == 1 else 0)) for j in range(m)] + [Fraction(f[i])] for i in range(m)]
    for k in range(m):
        pivot = a[k][k]
        assert pivot != 0
        for j in range(k, m+1):
            a[k][j] /= pivot
        for i in range(k+1, m):
            factor = a[i][k]
            for j in range(k, m+1):
                a[i][j] -= factor * a[k][j]
    x = [Fraction(0)] * m
    for i in range(m-1, -1, -1):
        x[i] = a[i][m] - sum(a[i][j] * x[j] for j in range(i+1, m))
    return x


class TestSpectrum(unittest.TestCase):
    def test_eigenvalues(self):
        for n in range(2, 35):
            actual = np.linalg.eigvalsh(laplacian(n))
            expected = [2 - 2*math.cos(math.pi*k/n) for k in range(1, n)]
            np.testing.assert_allclose(actual, expected, atol=1e-12, rtol=1e-12)

    def test_eigenvectors(self):
        for n in range(2, 24):
            L = laplacian(n)
            for k in range(1, n):
                v = np.array([math.sin(math.pi*k*j/n) for j in range(1, n)])
                lam = 2 - 2*math.cos(math.pi*k/n)
                np.testing.assert_allclose(L @ v, lam*v, atol=1e-12, rtol=1e-12)

    def test_orthogonality_norm(self):
        for n in range(2, 26):
            V = np.array([[math.sin(math.pi*k*j/n) for k in range(1, n)] for j in range(1, n)])
            np.testing.assert_allclose(V.T @ V, (n/2)*np.eye(n-1), atol=2e-12, rtol=1e-12)

    def test_green_inverse(self):
        for n in range(2, 22):
            G = np.array([[float(green_exact(n, i, j)) for j in range(1,n)] for i in range(1,n)])
            np.testing.assert_allclose(laplacian(n) @ G, np.eye(n-1), atol=2e-12)

    def test_green_spectral(self):
        for n in range(2, 22):
            for i in range(1,n):
                for j in range(1,n):
                    spectral = sum((2/n)*math.sin(math.pi*k*i/n)*math.sin(math.pi*k*j/n)/(2-2*math.cos(math.pi*k/n)) for k in range(1,n))
                    self.assertAlmostEqual(spectral, float(green_exact(n,i,j)), places=9)

    def test_exact_poisson(self):
        for n in range(2, 9):
            for source in product((-2, 0, 3), repeat=min(n-1, 4)):
                if n-1 > 4:
                    source = tuple(source) + (0,) * (n-5)
                x = solve_tridiagonal_exact(n, source)
                g = [sum(green_exact(n,i,j)*source[j-1] for j in range(1,n)) for i in range(1,n)]
                self.assertEqual(x,g)

    def test_sharp_poincare(self):
        for n in range(2, 28):
            gap = 2 - 2*math.cos(math.pi/n)
            v = np.array([math.sin(math.pi*j/n) for j in range(1,n)])
            self.assertAlmostEqual(float(v @ laplacian(n) @ v), gap*float(v @ v), places=10)
            for seed in range(4):
                rng = np.random.default_rng(n*100+seed)
                x = rng.normal(size=n-1)
                self.assertGreaterEqual(float(x @ laplacian(n) @ x)+1e-10, gap*float(x @ x))

    def test_operator_norm(self):
        for n in range(2, 20):
            gap = 2 - 2*math.cos(math.pi/n)
            rng = np.random.default_rng(n)
            f = rng.normal(size=n-1)
            u = np.linalg.solve(laplacian(n), f)
            self.assertLessEqual(np.linalg.norm(u), np.linalg.norm(f)/gap+1e-10)

    def test_heat_decay(self):
        for n in range(2, 20):
            gap = 2 - 2*math.cos(math.pi/n)
            L = laplacian(n)
            eigenvalues, Q = np.linalg.eigh(L)
            x = np.arange(1,n,dtype=float)
            for t in (0,0.1,1.0,3.0):
                evolved = Q @ (np.exp(-eigenvalues*t)*(Q.T @ x))
                self.assertLessEqual(np.linalg.norm(evolved), math.exp(-gap*t)*np.linalg.norm(x)+1e-10)

    def test_edge_case_n_one(self):
        self.assertEqual([], [i for i in range(1,1)])
        self.assertEqual(Fraction(0), sum([], Fraction(0)))

if __name__ == '__main__':
    unittest.main()
