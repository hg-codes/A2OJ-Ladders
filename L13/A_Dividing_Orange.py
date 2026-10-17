n,k = map(int, input().split())
a = list(map(int, input().split()))

vis = [False]*(n*k+1)

for num in a:
    vis[num] = True

ans = [[] for _ in range(k)]

for i in range(k):
    ans[i].append(a[i])
    for j in range(1,n*k+1):
        if not vis[j] and len(ans[i]) < n:
            ans[i].append(j)
            vis[j] = True

for t in ans:
    print(*t)