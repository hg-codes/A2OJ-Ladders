n,k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

mx = -1e9

for [a,b] in l:
    if b>k:
        mx = max(mx,a-b+k)
    else:
        mx = max(mx,a)

print(mx)