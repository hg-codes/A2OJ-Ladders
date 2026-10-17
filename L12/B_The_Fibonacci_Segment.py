n = int(input())
l = list(map(int, input().split()))

mx = min(n,2)
count = mx

for i in range(2,n):
    if l[i] == l[i-1] + l[i-2]:
        count += 1
        mx = max(count,mx)
    else:
        count = min(n,2)

print(mx)