n = int(input())
best = None

# 4a + 7b = n
for b in range(n // 7 + 1):
    if (n - 7*b) % 4 == 0:
        a = (n - 7*b) // 4
        if best is None or a+b < sum(best):
            best = (a, b)

if best is None:
    print(-1)
else:
    a, b = best
    print('4'*a + '7'*b)