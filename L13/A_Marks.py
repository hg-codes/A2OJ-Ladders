n, m = map(int, input().split())
l = [list(map(int, list(input()))) for _ in range(n)]

mx = [0]*m
for i in range(n):
    for j in range(m):
        if l[i][j] > mx[j]:
            mx[j] = l[i][j]

ans = 0
for i in range(n):
    for j in range(m):
        if l[i][j] >= mx[j]:
            ans += 1
            break

print(ans)