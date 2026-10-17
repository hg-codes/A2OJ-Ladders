n,m,k = map(int, input().split())

l = []
for i in range(1,n+1):
    if i%2:
        for j in range(1,m+1):
            l.append((i,j))
    else:
        for j in range(m,0,-1):
            l.append((i,j))

i = 0
for _ in range(k-1):
    print(2, *l[i], *l[i+1])
    i += 2

ans = []
for a,b in l[i:]:
    ans.append(a)
    ans.append(b)

print(n*m- 2*(k-1), *ans)