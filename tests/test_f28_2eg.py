"""F28.2-EG: exact rational regression for weighted stability."""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt

def cost(x, w, cuts):
    n = len(x)
    bounds = (0,) + tuple(cuts) + (n,)
    total = F(0)
    for a, b in zip(bounds, bounds[1:]):
        mass = sum(w[a:b])
        mean = sum((w[i] * x[i] for i in range(a, b)), F(0)) / mass
        total += sum((w[i] * (x[i] - mean)**2 for i in range(a, b)), F(0))
    return total

def sqnorm(x, w):
    return sum((wi * xi * xi for xi, wi in zip(x, w)), F(0))

def partitions(n, k):
    return combinations(range(1, n), k - 1)

def check():
    checks = 0
    for n in range(2, 5):
        for vals in combinations(range(-2, 5), n):
            x = tuple(map(F, vals))
            for weights in product((F(1), F(2)), repeat=n):
                for k in range(1, n + 1):
                    ps = list(partitions(n, k))
                    ex = [cost(x, weights, p) for p in ps]
                    best = min(ex)
                    for shift in (-F(1, 3), F(0), F(1, 3)):
                        y = x[:-1] + (x[-1] + shift,)
                        # Last-coordinate perturbation preserves order for distinct integer samples.
                        d2 = sqnorm(tuple(a-b for a,b in zip(x,y)), weights)
                        ey = [cost(y, weights, p) for p in ps]
                        for a,b in zip(ex,ey):
                            # (sqrt(a)-sqrt(b))^2 <= d^2, without floating point:
                            assert (a+b-d2)**2 <= 4*a*b if a+b>=d2 else True
                            checks += 1
                            # |b-a| <= 2 sqrt(a*d2)+d2, square after subtracting d2.
                            if abs(b-a)>d2:
                                assert (abs(b-a)-d2)**2 <= 4*a*d2
                            checks += 1
                        v = min(ey)
                        assert (best+v-d2)**2 <= 4*best*v if best+v>=d2 else True
                        checks += 1
    assert cost((F(0),F(1),F(3)),(F(1),)*3,(2,)) == F(1,2)
    assert cost((F(0),F(1),F(3)),(F(1),)*3,(1,)) == F(2)
    print(f"PASS: {checks} exact rational assertions")
if __name__ == "__main__":
    check()
