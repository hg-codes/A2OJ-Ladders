import sys
input = sys.stdin.readline
n = int(input())

a = g = 0
ans = []
for _ in range(n):
    x, y = map(int, input().split())
    if g + x - a <= 500:
        g += x
        ans.append("A")
    else:
        a += y
        ans.append("G")

print("".join(ans))