from fractions import Fraction as F
from itertools import product

def energy(items):
    w=sum((a for a,b in items),F(0))
    m=sum((a*b for a,b in items),F(0))/w
    return sum((a*(b-m)**2 for a,b in items),F(0))

def check(blocks):
    allitems=sum(blocks,[])
    ws=[sum((w for w,x in b),F(0)) for b in blocks]
    ms=[sum((w*x for w,x in b),F(0))/W for b,W in zip(blocks,ws)]
    W=sum(ws,F(0))
    M=sum((w*m for w,m in zip(ws,ms)),F(0))/W
    within=sum((energy(b) for b in blocks),F(0))
    between=sum((w*(m-M)**2 for w,m in zip(ws,ms)),F(0))
    pairs=sum((ws[i]*ws[j]*(ms[i]-ms[j])**2 for i in range(len(ws)) for j in range(i+1,len(ws))),F(0))/W
    assert energy(allitems)==within+between
    assert between==pairs
    assert between>=0
    assert (between==0)==(len(set(ms))==1)
    return 4

def main():
    count=0
    for n in (2,3,4):
        for xs in product((-2,0,3),repeat=n):
            for weights in product((1,2),repeat=n):
                items=[(F(w),F(x)) for w,x in zip(weights,xs)]
                for labels in product(range(2),repeat=n):
                    if len(set(labels))!=2: continue
                    blocks=[[item for item,l in zip(items,labels) if l==j] for j in range(2)]
                    count+=check(blocks)
                if n>=3:
                    for labels in product(range(3),repeat=n):
                        if len(set(labels))!=3: continue
                        blocks=[[item for item,l in zip(items,labels) if l==j] for j in range(3)]
                        count+=check(blocks)
    print("PASS exact rational assertions:",count)

if __name__=="__main__":
    main()
