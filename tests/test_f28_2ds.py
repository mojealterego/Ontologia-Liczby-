from fractions import Fraction as F
from itertools import product

def test_discrete_quantile_certificates():
    checks = 0
    for n in (2, 3, 4, 5):
        for vals in product(range(4), repeat=n):
            if list(vals) != sorted(vals):
                continue
            q = [F(x) for x in vals]
            for k in range(1, n + 1):
                if n % k:
                    continue
                blocks = [q[i:i+k] for i in range(0, n, k)]
                means = [sum(b)/len(b) for b in blocks]
                l1 = sum(sum(abs(x-m) for x in b) for b,m in zip(blocks, means))/n
                l2 = sum(sum((x-m)**2 for x in b) for b,m in zip(blocks, means))/n
                D = q[-1]-q[0]
                h = F(k, n)
                assert l1*l1 <= l2
                assert l1 <= h*D/2
                assert l2 <= h*D*D/4
                assert sum(q) == sum(m*len(b) for b,m in zip(blocks,means))
                checks += 4
    assert checks == 1108

if __name__ == "__main__":
    test_discrete_quantile_certificates()
    print("PASS: 1109 exact assertions including assertion count")
