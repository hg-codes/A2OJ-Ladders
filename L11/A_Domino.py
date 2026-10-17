n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

uo = sum(x%2 for [x,y] in l)
lo = sum(y%2 for [x,y] in l)
pair_exist = any(x%2!=y%2 for x,y in l)

if uo%2 == lo%2 == 0:
    print(0)
elif pair_exist and uo%2 and lo%2:
        print(1)
else:
    print(-1)