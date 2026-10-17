y,k,n = map(int,input().split())
ans = []

xpluxy = (y//k + 1)*k

while xpluxy <= n:
    ans.append(xpluxy-y)
    xpluxy += k

if len(ans) > 0:
    print(*ans)
else:
    print(-1)