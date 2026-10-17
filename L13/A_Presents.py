n = int(input())
a = list(map(int, input().split()))

ans = [0]*(n+1)
for i, num in enumerate(a):
    ans[num] = i+1

print(*ans[1:])