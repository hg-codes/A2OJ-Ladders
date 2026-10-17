n = int(input())
l = [list(map(int,input().split())) for i in range(n)]

mn,mx = 1e9,0

for [a,b] in l:
    mn = min(mn,a)
    mx = max(mx,b)

if [mn,mx] in l:
    print(l.index([mn,mx])+1)
else:
    print(-1)