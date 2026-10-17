n,m = map(int, input().split())
l = list(map(int, input().split()))

f = 0
for _ in range(m):
    o = list(map(int, input().split()))
    if o[0]==1:
        l[o[1]-1] = o[2]-f
    elif o[0]==2:
        f += o[1]
    else:
        print(l[o[1]-1]+f)