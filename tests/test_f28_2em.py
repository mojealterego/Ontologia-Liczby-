"""F28.2-EM: exact arithmetic regression tests; stdlib only."""
from fractions import Fraction as F
from itertools import product

def cost(x, w, blocks):
    total = F(0)
    for block in blocks:
        sw = sum((w[i] for i in block), F(0))
        assert sw > 0
        mean = sum((w[i]*x[i] for i in block), F(0))/sw
        total += sum((w[i]*(x[i]-mean)**2 for i in block), F(0))
    return total

def run():
    checks = 0
    for n in (2, 3, 4):
        for x0 in product((-1, 0, 2), repeat=n):
            x = tuple(map(F, x0))
            w = tuple(F(i+1) for i in range(n))
            for mask in range(1 << (n-1)):
                blocks = []
                start = 0
                for j in range(n-1):
                    if mask & (1 << j):
                        blocks.append(tuple(range(start,j+1)))
                        start = j+1
                blocks.append(tuple(range(start,n)))
                c = cost(x,w,blocks)
                assert c >= 0
                checks += 1
                for shift in (-3, 1, 4):
                    y = tuple(v+shift for v in x)
                    assert cost(y,w,blocks) == c
                    checks += 1
                h = [F(0)]*n
                for index, block in enumerate(blocks):
                    for i in block:
                        h[i] = F(index+2)
                for t in (-2, 0, 3):
                    assert cost(tuple(x[i]+t*h[i] for i in range(n)),w,blocks) == c
                    checks += 1
    assert cost((F(0),F(2),F(7)),(F(1),F(1),F(2)),((0,1),(2,))) == 2
    assert cost((F(0),F(4)),(F(1),F(3)),((0,1),)) == 12
    print("PASS", checks+2, "exact checks")
if __name__ == "__main__":
    run()
