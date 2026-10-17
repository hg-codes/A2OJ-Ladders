# n = int(input())
# l = [tuple(map(int, input().split())) for _ in range(n)]
# l.sort()

# mx = count = 1
# for i in range(1,n):
#     count = count + 1 if l[i] == l[i-1] else 1
#     mx = max(mx, count)
# print(mx)

from collections import Counter

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

print(max(Counter(a).values()))