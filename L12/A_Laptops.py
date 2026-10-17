def Y(): print("Happy Alex")
def N(): print("Poor Alex")

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()

mn = 0
for [a,b] in l:
    if b > mn:
        mn = b
    else:
        Y()
        break
else:
    N()