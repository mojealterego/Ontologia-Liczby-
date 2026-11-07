from fractions import Fraction
from math import log

def solve(a, y0, u):
    y = Fraction(y0)
    out = [y]
    for n, forcing in enumerate(u):
        y = Fraction(n + 1, n + 1 + a) * y + forcing
        out.append(y)
    return out

def product(a, m, n):
    p = Fraction(1)
    for j in range(m, n):
        p *= Fraction(j + 1, j + 1 + a)
    return p

def test_exact():
    checks = 0
    for a in (1, 2, 3, 5):
        for y0 in (-3, 0, 2):
            for c in (-2, 0, 4):
                u = [Fraction(c, n + 1 + a) for n in range(24)]
                ys = solve(a, y0, u)
                for n, y in enumerate(ys):
                    assert y == Fraction(c, a) + product(a, 0, n) * (Fraction(y0) - Fraction(c, a))
                    checks += 1
                for n in range(1, len(ys)):
                    assert ys[n] == product(a, 0, n) * y0 + sum(
                        (product(a, j + 1, n) * u[j] for j in range(n)), Fraction(0)
                    )
                    checks += 1
    return checks

def test_asymptotic():
    checks = 0
    for a in (1., 2., 4.):
        for q in (-1., 0., 1.):
            y = 0.
            nmax = 100000
            for n in range(nmax):
                y = (n + 1) / (n + 1 + a) * y + 1 / ((n + 2) * log(n + 2) ** q)
            target = log(nmax) ** (-q) / a
            assert abs(y / target - 1) < 0.13, (a, q, y, target)
            checks += 1
    return checks

if __name__ == "__main__":
    n = test_exact() + test_asymptotic()
    print("PASS", n, "assertions")
