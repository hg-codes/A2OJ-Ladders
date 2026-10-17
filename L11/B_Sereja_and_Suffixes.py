n,m = map(int, input().split())
l = list(map(int, input().split()))
t = [int(input())-1 for i in range(m)]

seen = set()
ans = [0] * n
cnt = 0

for i in range(n - 1, -1, -1):
    if l[i] not in seen:
        cnt += 1
        seen.add(l[i])
    ans[i] = cnt

for i in t:
    print(ans[i])