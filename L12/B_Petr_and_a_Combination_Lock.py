def solve():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    for mask in range(1 << n):
        total = 0
        for j in range(n):
            if mask >> j & 1:
                total -= a[j]
            else:
                total += a[j]

        if total % 360 == 0:
            print("YES")
            return
    print("NO")

solve()