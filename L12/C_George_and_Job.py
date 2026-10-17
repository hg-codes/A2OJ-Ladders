n, m, k = map(int, input().split())
p = list(map(int, input().split()))

if m==1:
    print(sum(sorted(p, reverse=True)[:k]))
    exit()

if m * k == n:
    print(sum(p))
    exit()

psum = [0] * (n + 1)
for i in range(1, n + 1):
    psum[i] = psum[i - 1] + p[i - 1]
 
dp = [[0] * (n + 1) for _ in range(k + 1)]
 
for i in range(1, k + 1):
    for j in range(1, n + 1):
 
        # Don't choose a segment ending at j
        dp[i][j] = dp[i][j - 1]
 
        # Choose segment [j-m+1 ... j]
        if j >= i * m:
            cur = psum[j] - psum[j - m]
            dp[i][j] = max(dp[i][j],
                            dp[i - 1][j - m] + cur)
 
print(dp[k][n])