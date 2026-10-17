n = int(input())
l = list(map(int,input().split()))

ans = 0
while n > 0:
    for i in range(7):
        ans = i + 1
        n -= l[i]
        if n <= 0:
            break

print(ans)