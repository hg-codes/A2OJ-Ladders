n = int(input())
doors = [list(map(int,input().split())) for _ in range(n)]

l = sum(d[0] for d in doors)
r = sum(d[1] for d in doors)

sum = min(l,n-l) + min(r,n-r)
print(sum)