n, m = map(int,input().split())
l = list(map(int,input().split()))

l.sort()

diff = 1000
for i in range(0,m-n+1):
    d = l[i+n-1] - l[i]
    if d < diff:
        diff = d

print(diff)