n = int(input())
a = list(map(int, input().split()))

pos = {}
ans = []

for i, x in enumerate(a):
    if x not in pos:
        pos[x] = []
    pos[x].append(i)

for x in pos:
    p = pos[x]
    l = len(p)

    if l == 1:
        ans.append((x, 0))
    else:
        d = p[1] - p[0]
        if all(p[i] - p[i-1] == d for i in range(2, l)):
            ans.append((x, d))

ans.sort()
print(len(ans))
for x, d in ans:
    print(x, d)