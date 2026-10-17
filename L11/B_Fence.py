n, k = map(int, input().split())
l = list(map(int, input().split()))

ps = sum(l[:k])
ans = 1
s = ps

for i in range(k,n):
    ps = ps + l[i] - l[i-k]
    if ps < s:
        ans = i - k + 2
    s = min(ps,s)
    
print(ans)