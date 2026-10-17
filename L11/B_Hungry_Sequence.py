MAX = 1300001

n = int(input())
prime = [True] * MAX

for i in range(2,int(MAX**0.5)+1):
    if prime[i]:
        prime[i*i:MAX:i] = [False] * ((MAX - 1 - i*i)//i + 1)

ans = []
for i in range(2,MAX):
    if prime[i]:
        ans.append(i)
        if len(ans) == n:
            break

print(*ans)