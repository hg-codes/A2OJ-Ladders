n, k = map(int, input().split())
MOD = 1000000007 
 
fact = [[] for _ in range(n+1)]
 
for i in range(1,n+1):
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            fact[i].append(j)
            if i//j != j:
                fact[i].append(i//j)
 
dp = [[0]*(n+1) for _ in range(k+1)]
# dp[i][j] = no of good arrays of length i ending in j
 
for i in range(1,n+1):
    dp[1][i] = 1
 
for i in range(2,k+1):
    for j in range(1,n+1):
        dp[i][j] = 0
        for f in fact[j]:
            dp[i][j] = (dp[i][j] + dp[i-1][f])%MOD
 
ans = 0
for i in range(1,n+1):
    ans = (ans + dp[k][i])%MOD
 
print(ans)