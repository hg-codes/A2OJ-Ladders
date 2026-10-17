k = int(input())
l = list(map(int, input().split()))

l.sort()
l = l[::-1]

i = 0

while k > 0 and i < 12:
    k -= l[i]
    i += 1

if k > 0:
    print(-1)
else:
    print(i)