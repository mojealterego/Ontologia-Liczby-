from fractions import Fraction as F
from itertools import combinations_with_replacement

def run():
    checks = 0
    for q in combinations_with_replacement(range(5), 6):
        x = list(map(F, q))
        for k in range(1, 6):
            ml = sum(x[:k]) / k
            mr = sum(x[k:]) / (6-k)
            m = sum(x) / 6
            old = sum((v-m)**2 for v in x) / 6
            new = (sum((v-ml)**2 for v in x[:k]) + sum((v-mr)**2 for v in x[k:])) / 6
            gain = F(k*(6-k), 36) * (ml-mr)**2
            assert old-new == gain
            assert 0 <= gain <= F(k*(6-k),36)*(max(x)-min(x))**2
            checks += 2
    print("PASS", checks, "exact assertions")

if __name__ == "__main__":
    run()
