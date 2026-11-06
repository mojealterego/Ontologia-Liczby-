from fractions import Fraction as F
from itertools import combinations, product

def cost(z, cuts):
    edges = (0,) + tuple(cuts) + (len(z),)
    result = F(0)
    for a, b in zip(edges, edges[1:]):
        block = z[a:b]
        mean = sum(block, F(0)) / len(block)
        result += sum(((v-mean)**2 for v in block), F(0))
    return result

def test_polynomial_identity():
    checks = 0
    for n in range(3, 6):
        for k in range(1, n + 1):
            for raw in product(range(3), repeat=n):
                x = tuple(map(F, sorted(raw)))
                directions = [(F(0),)*n, tuple(F(i % 2) for i in range(n)), tuple(F(i) for i in range(n))]
                for h in directions:
                    for cuts in combinations(range(1, n), k - 1):
                        a = cost(h, cuts)
                        c = cost(x, cuts)
                        b = cost(tuple(x[i]+h[i] for i in range(n)), cuts)-a-c
                        for t in (F(0), F(1,2), F(1), F(2)):
                            z = tuple(x[i]+t*h[i] for i in range(n))
                            assert cost(z, cuts) == a*t*t+b*t+c
                            checks += 1
    assert checks == 55728
    assert cost((F(0),F(1),F(2)), (1,)) == F(1,2)
    assert cost((F(0),F(1),F(2)), (2,)) == F(1,2)

if __name__ == "__main__":
    test_polynomial_identity()
    print("PASS: 55728 exact rational identities")
