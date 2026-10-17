n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

s = 0

for i in range(n):
    su = sum(l[i])
    if su > 1:
        s += 1

print(s)