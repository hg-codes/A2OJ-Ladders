def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    i = 0
    while i < n:
        mx = a[i]
        while i + 1 < n and (a[i] >= 0) == (a[i + 1] >= 0):
            i += 1
            mx = max(mx, a[i])
        ans += mx
        i += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()