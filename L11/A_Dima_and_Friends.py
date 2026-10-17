n = int(input())
l = list(map(int,input().split()))
s = sum(l)

op = [1,2,3,4,5]
ans = 0

for o in op:
    sf = s + o
    while sf > (n + 1):
        sf -= (n + 1)
    if sf != 1:
        ans += 1

print(ans)