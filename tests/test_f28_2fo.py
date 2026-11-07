from fractions import Fraction as F

def run(a, y0, inputs):
    y=F(y0); out=[y]
    for k,u in enumerate(inputs):
        y=F(k+1,k+1+a)*y+F(u)
        out.append(y)
    return out

checks=0
for a in (1,2,3,5):
    for y0 in (-3,0,2):
        for b in (-2,0,3):
            n=40
            u=[F(b,k+1+a) for k in range(n)]
            ys=run(a,y0,u)
            prod=F(1)
            for k in range(n+1):
                assert ys[k]==F(b,a)+prod*(F(y0)-F(b,a))
                checks+=1
                if k<n: prod*=F(k+1,k+1+a)
            for k in range(n):
                assert ys[k+1]==F(k+1,k+1+a)*ys[k]+u[k]
                checks+=1
for n in range(1,70):
    ys=run(1,0,[F(1,k+1) for k in range(n)])
    harmonic=sum((F(1,r) for r in range(1,n+1)),F(0))
    assert ys[-1]==F(n, n+1)+harmonic/F(n+1)
    checks+=1
print("PASS exact rational checks:",checks)
