x,y, a,b = map(int, input().split())

tot = 0
ans = []
for i in range(b,y+1):
    for j in range(a,x+1):
        if j>i:
            tot += 1
            ans.append([j,i])

ans.sort()
print(tot)
for a,b in ans:
    print(a,b)