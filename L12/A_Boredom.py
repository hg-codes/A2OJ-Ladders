n = int(input())
a = list(map(int, input().split()))

MAX_NUM = max(a)
cnt = [0]*(MAX_NUM + 1)

for num in a:
    cnt[num] += 1

f = [0]*(MAX_NUM + 1)
f[1] = cnt[1]
for i in range(2, MAX_NUM + 1):
    f[i] = max(f[i-1], f[i-2] + cnt[i]*i)

print(f[MAX_NUM])