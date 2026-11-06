from fractions import Fraction as F
from itertools import product

def cost(x,w,blocks):
    total=F(0)
    for b in blocks:
        W=sum((w[i] for i in b),F(0))
        mean=sum((w[i]*x[i] for i in b),F(0))/W
        total+=sum((w[i]*(x[i]-mean)**2 for i in b),F(0))
    return total

def main():
    checked=0
    for n in range(2,6):
        for values in product((-1,0,2),repeat=n):
            x=list(map(F,values))
            for weights in product((1,2),repeat=n):
                w=list(map(F,weights))
                for cut in range(1,n):
                    A=list(range(cut)); B=list(range(cut,n))
                    wa=sum(w[:cut]); wb=sum(w[cut:])
                    ma=sum((w[i]*x[i] for i in A),F(0))/wa
                    mb=sum((w[i]*x[i] for i in B),F(0))/wb
                    expected=wa*wb/(wa+wb)*(ma-mb)**2
                    assert cost(x,w,[A+B])-cost(x,w,[A,B])==expected
                    checked+=1
    assert checked==35460
    print("PASS",checked)

if __name__=="__main__":
    main()
