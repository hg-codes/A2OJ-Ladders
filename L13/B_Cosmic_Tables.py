import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
r = list(range(n+1))
c = list(range(m+1))

ans = []
for _ in range(k):
    s,x,y = list(input().split())
    x,y = int(x), int(y)
    if s=='r':
        r[x],r[y] = r[y],r[x]
    elif s=='c':
        c[x],c[y] = c[y],c[x]
    else:
        ans.append(str(l[r[x]-1][c[y]-1]))

print("\n".join(ans))