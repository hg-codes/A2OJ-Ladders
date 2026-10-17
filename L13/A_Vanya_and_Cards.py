n, x = map(int, input().split())
a = list(map(int, input().split()))

s = abs(sum(a))
ans = 0
while s>0:
    s -= x
    ans += 1

print(ans)