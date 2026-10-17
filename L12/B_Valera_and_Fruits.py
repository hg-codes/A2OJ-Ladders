n,v = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(reverse=True)

ans = [0]*(3002)

for [a,b] in l:
    fr = v-ans[a+1]
    if b>fr:
        ans[a+1] = v
        b -= fr
        ans[a] = min(v, ans[a]+b)
    else:
        ans[a+1] += b

print(sum(ans))