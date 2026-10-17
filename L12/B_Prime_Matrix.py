from bisect import bisect_left
n,m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

N = 100005
prime = [True]*N
prime[0] = prime[1] = False

for i in range(2,int(N**0.5 + 1)):
    if prime[i]:
        x = prime[i*i:N:i]
        prime[i*i:N:i] = [False] * len(x)

p = [i for i in range(2, N) if prime[i]]

for i in range(n):
    for j in range(m):
        k = bisect_left(p, mat[i][j])
        mat[i][j] = p[k] - mat[i][j]

ans = 10**9
for i in range(n):
    ans = min(sum(mat[i]),ans)

for j in range(m):
    s = 0
    for i in range(n):
        s += mat[i][j]
    ans = min(s,ans)

print(ans)