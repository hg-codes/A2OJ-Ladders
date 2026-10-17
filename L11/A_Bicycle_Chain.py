n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

l = []
for i in range(n):
    for j in range(m):
        r = b[j]//a[i]
        ri = b[j]/a[i]
        if r == ri:
            l.append(r)

print(l.count(max(l)))