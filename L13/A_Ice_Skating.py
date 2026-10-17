n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = [False] * n

l = [set() for _ in range(n)]
for i in range(n):
    x, y = a[i]
    for j in range(n):
        if i == j:
            continue
        x1, y1 = a[j]
        if x1 == x or y1 == y:
            l[i].add(j)

count = 0
for i in range(n):
    if not ans[i]:
        count += 1
        stack = [i]
        ans[i] = True

        while stack:
            u = stack.pop()
            for v in l[u]:
                if not ans[v]:
                    ans[v] = True
                    stack.append(v)

print(count - 1)