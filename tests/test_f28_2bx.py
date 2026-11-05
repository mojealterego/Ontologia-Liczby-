from fractions import Fraction as F
from itertools import product

def H(atoms,t):
    result=F(0); remaining=t
    for x,p in sorted(atoms,reverse=True):
        q=min(remaining,p)
        result+=x*q
        remaining-=q
        if remaining==0: break
    assert remaining==0
    return result

def test_grid_reconstruction_and_error():
    count=0
    for vals in product(range(-2,4),repeat=3):
        for w1 in range(5):
            for w2 in range(5-w1):
                weights=[F(w1,4),F(w2,4),F(4-w1-w2,4)]
                atoms=list(zip(map(F,vals),weights))
                grid=[F(i,4) for i in range(5)]
                y=[H(atoms,t) for t in grid]
                slopes=[4*(y[i+1]-y[i]) for i in range(4)]
                assert all(slopes[i]>=slopes[i+1] for i in range(3))
                assert all(F(-2)<=s<=F(3) for s in slopes)
                assert y[0]==0 and y[-1]==sum(x*p for x,p in atoms)
                reconstructed=list(zip(slopes,[F(1,4)]*4))
                for i,t in enumerate(grid):
                    assert H(reconstructed,t)==y[i]
                for t in [F(i,16) for i in range(17)]:
                    j=min(int(4*t),3)
                    L=y[j]+slopes[j]*(t-grid[j])
                    actual=H(atoms,t)
                    assert L<=actual<=L+F(5,16)
                    count+=1
    assert count==55080

if __name__=='__main__':
    test_grid_reconstruction_and_error()
    print('PASS: 55080 exact rational checks')
