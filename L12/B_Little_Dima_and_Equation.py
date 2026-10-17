def func(n):
    return sum(map(int, str(n)))

a,b,c = map(int, input().split())

ans = []
for i in range(1,83):
    n = b*(i**a)+c
    if 0 < n < 1e9 and func(n)==i:
        ans.append(n)

print(len(ans))
if len(ans):
    print(*ans)