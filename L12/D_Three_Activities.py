def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a = sorted([(x, i) for i, x in enumerate(a)], reverse=True)[:3]
    b = sorted([(x, i) for i, x in enumerate(b)], reverse=True)[:3]
    c = sorted([(x, i) for i, x in enumerate(c)], reverse=True)[:3]

    ans = 0
    for x, i in a:
        for y, j in b:
            for z, k in c:
                if i != j and j != k and i != k:
                    ans = max(ans, x + y + z)
    print(ans)

t = int(input())
for _ in range(t):
    solve()