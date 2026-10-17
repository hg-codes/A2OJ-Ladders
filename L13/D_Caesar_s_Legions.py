from functools import lru_cache

MOD = 100000000
n1,n2,k1,k2 = map(int, input().split())
l1,l2 = k1,k2

@lru_cache(None)
def getAns(n1,n2,k1,k2):
    if n1==0 and n2==0:
        return 1
    
    x,y = 0,0
    if n1>0 and k1>0:
        x = getAns(n1-1,n2,k1-1,l2)
    
    if n2>0 and k2>0:
        y = getAns(n1,n2-1,l1,k2-1)

    return (x+y)%MOD

print(getAns(n1,n2,k1,k2))