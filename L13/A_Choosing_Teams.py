n,k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for num in a:
    if num <= 5-k:
        ans += 1

print(ans//3)