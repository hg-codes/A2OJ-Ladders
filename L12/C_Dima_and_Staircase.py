n = int(input())
a = list(map(int, input().split()))
m = int(input())
mat = [list(map(int, input().split())) for _ in range(m)]

L,h = 0, 0
for [w,nh] in mat:
    L = max(L + h, a[w - 1])
    print(L)
    h = nh