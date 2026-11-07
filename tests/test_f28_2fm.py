from fractions import Fraction as F
from itertools import product

def run():
    checks=0
    for a in (F(0),F(1,2),F(-1,3)):
        for u,v in product(range(-2,3),repeat=2):
            x,y=F(u),F(v)
            sx=F(0)
            yy=F(v)
            for k in range(1,9):
                d=F((-1)**k,k+1)
                n=F(1,2**k)
                sx+=d
                yy=a*yy+n
                x+=d
                y=a*y+n
                assert x==F(u)+sx
                assert y==yy
                checks+=2
    print(f"PASS: {checks} exact rational assertions")

if __name__=="__main__":
    run()
