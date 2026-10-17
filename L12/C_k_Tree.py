MOD = 1000000007
n, k, d = map(int, input().split())

dp = [[0, 0] for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for x in range(1, k + 1):
        if i - x < 0:
            continue
        if x < d:
            dp[i][0] += dp[i-x][0]
            dp[i][1] += dp[i-x][1]
        else:
            dp[i][1] += dp[i-x][0] + dp[i-x][1]

        dp[i][0] %= MOD
        dp[i][1] %= MOD

print(dp[n][1])