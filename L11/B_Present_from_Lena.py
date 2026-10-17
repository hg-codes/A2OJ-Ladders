n = int(input())

s = 2*n - 1
l = list(range(n)) + list(range(n, -1, -1))

for i in range(n):
    print(" "*(s), *l[:i+1], *l[:i][::-1])
    s -= 2

print(*l)

for i in range(n-1,-1,-1):
    s += 2
    print(" "*(s), *l[:i+1], *l[:i][::-1])