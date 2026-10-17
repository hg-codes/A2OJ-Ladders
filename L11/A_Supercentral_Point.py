n = int(input())
x, y = [], []

for i in range(n):
    a,b = map(int,input().split())
    x.append((a,b))
    y.append((b,a))

x.sort()
y.sort()

r = {(x[i][0], x[i][1]) for i in range(1,n-1) if x[i][0] == x[i-1][0] == x[i+1][0]}
u = {(y[i][1], y[i][0]) for i in range(1,n-1) if y[i][0] == y[i-1][0] == y[i+1][0]}

print(len(r & u))