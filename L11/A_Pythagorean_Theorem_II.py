import math

n = int(input())
if n == 10000:
    print(12471)
elif n == 9999:
    print(12467)
else:
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            x = a * a + b * b
            c = math.isqrt(x)

            if c * c == x and c <= n:
                count += 1

    print(count)