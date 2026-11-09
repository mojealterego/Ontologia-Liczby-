from fractions import Fraction as F
from itertools import product

def radius(vertices, cost, x):
    return min((sum(c*(v-xj) for c,v,xj in zip(cost,w,x))/sum(abs(v-xj) for v,xj in zip(w,x)) for w in vertices if w!=x), default=None)

def test():
    count=0
    for n in (2,3):
        verts=[tuple(F(int(i==j)) for i in range(n)) for j in range(n)]
        for cs in product(range(-3,4),repeat=n):
            c=tuple(map(F,cs)); m=min(cs)
            for i in range(n):
                if cs[i]!=m:continue
                x=verts[i]; expected=min((F(cs[j]-cs[i],2) for j in range(n) if j!=i),default=None)
                assert radius(verts,c,x)==expected
                for e in product(range(-2,3),repeat=n):
                    ep=tuple(F(t,2) for t in e)
                    if expected is not None and max(map(abs,ep))<expected:
                        assert all(sum((c[k]+ep[k])*(v[k]-x[k]) for k in range(n))>=0 for v in verts)
                    count+=1
    print('PASS',count,'exact perturbation comparisons')
if __name__=='__main__':test()
