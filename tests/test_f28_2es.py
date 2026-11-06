from fractions import Fraction as F
from itertools import product

def energy(items):
    w = sum((a for a, _ in items), F(0))
    m = sum((a*x for a, x in items), F(0))/w
    return sum((a*(x-m)**2 for a,x in items), F(0))

def check(A,B,i,j):
    u,p=A[i]; v,q=B[j]
    wa=sum((w for w,x in A),F(0)); wb=sum((w for w,x in B),F(0))
    ra=wa-u; rb=wb-v
    assert ra>0 and rb>0
    alpha=sum((w*x for k,(w,x) in enumerate(A) if k!=i),F(0))/ra
    beta=sum((w*x for k,(w,x) in enumerate(B) if k!=j),F(0))/rb
    cert=v*ra/(ra+v)*(q-alpha)**2+u*rb/(rb+u)*(p-beta)**2-u*ra/wa*(p-alpha)**2-v*rb/wb*(q-beta)**2
    aa=A[:i]+[B[j]]+A[i+1:]
    bb=B[:j]+[A[i]]+B[j+1:]
    delta=energy(aa)+energy(bb)-energy(A)-energy(B)
    assert cert==delta
    assert energy(A)+energy(B)-energy(aa)-energy(bb)==-delta
    for scale,offset in ((F(3),F(-7)),(F(-2),F(5))):
        f=lambda C:[(w,scale*x+offset) for w,x in C]
        assert energy(f(aa))+energy(f(bb))-energy(f(A))-energy(f(B))==scale**2*delta
    return 4

def run():
    n=0
    for vals in product((F(0),F(1),F(3)),repeat=4):
        for weights in product((F(1),F(2)),repeat=4):
            A=list(zip(weights[:2],vals[:2]))
            B=list(zip(weights[2:],vals[2:]))
            for i in range(2):
                for j in range(2):
                    n+=check(A,B,i,j)
    assert energy([(F(1),F(0)),(F(1),F(1))])+energy([(F(1),F(9)),(F(1),F(10))])==1
    print(f"PASS: {n} exact checks")

if __name__=="__main__":
    run()
