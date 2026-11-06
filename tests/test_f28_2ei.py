from fractions import Fraction as F
from itertools import combinations, product

def cost(x, cuts):
    ends = (0,) + tuple(cuts) + (len(x),)
    total = F(0)
    for left, right in zip(ends, ends[1:]):
        mean = sum(x[left:right], F(0)) / (right-left)
        total += sum(((v-mean)**2 for v in x[left:right]), F(0))
    return total

def test_directional_identity():
    checks = 0
    for n in (3, 4, 5):
        for values in combinations(range(8), n):
            x = tuple(map(F, values))
            partitions = list(combinations(range(1, n), 1))
            best = min(partitions, key=lambda p: cost(x, p))
            if sum(cost(x, p) == cost(x, best) for p in partitions) != 1:
                continue
            for hv in product((-1, 0, 1), repeat=n):
                h = tuple(map(F, hv))
                for q in partitions:
                    if q == best:
                        continue
                    c = cost(x, q)-cost(x, best)
                    plus = tuple(x[i]+h[i] for i in range(n))
                    minus = tuple(x[i]-h[i] for i in range(n))
                    b = (cost(plus,q)-cost(plus,best)-cost(minus,q)+cost(minus,best))/2
                    a = cost(h,q)-cost(h,best)
                    for t in (F(0), F(1,3), F(1,2)):
                        y = tuple(x[i]+t*h[i] for i in range(n))
                        assert cost(y,q)-cost(y,best) == c+b*t+a*t*t
                        checks += 1
    x = (F(0), F(1), F(3))
    h = (F(0), F(0), F(-2))
    assert cost(x,(2,)) == F(1,2)
    assert cost(x,(1,)) == 2
    y = tuple(x[i]+h[i]/2 for i in range(3))
    assert cost(y,(1,)) == cost(y,(2,))
    return checks

if __name__ == '__main__':
    print('PASS',test_directional_identity(),'exact identities')
