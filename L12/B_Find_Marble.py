n,s,f = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n+1):
    if s == f:
        print(i)
        break
    s = l[s-1]
else:
    print(-1)
