n = int(input())
a = list(map(int, input().split()))
b = [1 if a[i] == 0 else -1 for i in range(n)]
ones = sum(a)

current = best = 0

for x in b:
    current = max(0, current + x)
    best = max(best, current)

if n-ones == 0:
    print(ones - 1)
else:
    print(ones + best)