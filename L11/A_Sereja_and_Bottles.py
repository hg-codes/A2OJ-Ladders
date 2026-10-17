n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
bottle = [False]*n

for i, [a,b] in enumerate(l):
    for j, [x,y] in enumerate(l):
        if i!=j and b==x:
            bottle[j] = True

print(sum(not b for b in bottle))