s, n = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]
l.sort()

flag = True

for [x,y] in l:
    if s > x:
        s += y
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")