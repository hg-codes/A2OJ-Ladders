n,m,d=map(int,input().split())
l=[x for _ in range(n) for x in map(int,input().split())]

if len({x%d for x in l})>1:
    print(-1)
else:
    l.sort()
    x=l[n*m//2]
    print(sum(abs(x-y)//d for y in l))