# n,a,b,c = map(int, input().split())
# dp = [-1] * (n + 1)
# dp[0] = 0

# for s in range(1, n + 1):
#     if s >= a and dp[s-a] != -1:
#         dp[s] = max(dp[s], dp[s-a] + 1)

#     if s >= b and dp[s-b] != -1:
#         dp[s] = max(dp[s], dp[s-b] + 1)

#     if s >= c and dp[s-c] != -1:
#         dp[s] = max(dp[s], dp[s-c] + 1)

# print(dp[n])

n,a,b,c = map(int,input().split())
a,b,c = sorted([a,b,c])[::-1]
ans = 0
 
for i in range(n//a+1):
	for j in range(n//b+1):
		k = (n-i*a-j*b)//c
		if i*a+b*j+k*c==n and k>=0:
			ans = max(ans,i+j+k)
			break
 
print(ans)