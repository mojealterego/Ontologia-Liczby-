from fractions import Fraction as F
from itertools import combinations_with_replacement

def check(q, n):
    N=len(q); k=2**n
    assert N%k==0
    size=N//k
    means=[sum(q[i:i+size],F(0))/size for i in range(0,N,size)]
    E=sum(((x-means[i//size])**2 for i,x in enumerate(q)),F(0))/N
    C=sum(((q[i+size-1]-q[i])**2 for i in range(0,N,size)),F(0))/(4*k)
    assert E<=C
    return E,C

def main():
    checks=0
    for q in combinations_with_replacement(range(4),8):
        q=list(map(F,q))
        e0,c0=check(q,0); e1,c1=check(q,1); e2,c2=check(q,2); e3,c3=check(q,3)
        assert e0>=e1>=e2>=e3==0
        assert e0-e1==sum((F(1,4)*(sum(q[i:i+2],F(0))/2-sum(q[i+2:i+4],F(0))/2)**2 for i in (0,4)),F(0))
        checks+=5
    assert check([F(i,8) for i in range(8)],0)[0]==F(21,256) # discrete grid variance
    print('PASS',checks+1,'exact rational assertions')

if __name__=='__main__': main()
