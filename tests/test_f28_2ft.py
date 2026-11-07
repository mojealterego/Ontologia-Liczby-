import unittest
from fractions import Fraction

def solve(a, y0, u):
    y = Fraction(y0)
    out = [y]
    for n, forcing in enumerate(u):
        y = Fraction(n + 1, n + 1 + a) * y + Fraction(forcing)
        out.append(y)
    return out

class TestFT(unittest.TestCase):
    def test_variation_constants(self):
        for a in (1, 2, 3, 5):
            for y0 in (-2, 0, 3):
                u = [Fraction((-1)**j, j+2) for j in range(20)]
                ys = solve(a, y0, u)
                H = [Fraction(1)]
                for n in range(20):
                    H.append(H[-1]*Fraction(n+1,n+1+a))
                for n in range(1,21):
                    rhs = H[n]*y0 + sum((H[n]/H[j+1]*u[j] for j in range(n)),Fraction(0))
                    self.assertEqual(ys[n],rhs)

    def test_abel_identity(self):
        for n in range(1,25):
            eps = [(-1)**j for j in range(n)]
            b = [Fraction(j*j+2, j+1) for j in range(n)]
            E = [sum(eps[:j+1]) for j in range(n)]
            lhs = sum((eps[j]*b[j] for j in range(n)),Fraction(0))
            rhs = E[-1]*b[-1] + sum((E[j]*(b[j]-b[j+1]) for j in range(n-1)),Fraction(0))
            self.assertEqual(lhs,rhs)

    def test_a1_examples(self):
        for n in range(1,60):
            alt = solve(1,0,[Fraction((-1)**j,j+2) for j in range(n)])[-1]
            self.assertEqual(alt,Fraction(n%2,n+1))
            raw = solve(1,0,[(-1)**j for j in range(n)])[-1]
            self.assertEqual(raw,Fraction(-n//2,n+1) if n%2==0 else Fraction((n-1)//2+2,n+1))

    def test_constant_forcing(self):
        for n in range(1,40):
            y=solve(1,0,[1]*n)[-1]
            self.assertEqual(y,Fraction(n*(n+3),2*(n+1)))

if __name__=="__main__":
    unittest.main()
