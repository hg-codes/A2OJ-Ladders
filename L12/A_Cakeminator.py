r,c=map(int,input().split())
a=[input() for _ in range(r)]

R=[i for i in range(r) if 'S' not in a[i]]
C=[j for j in range(c) if all(a[i][j]!='S' for i in range(r))]

print(len(R)*c+len(C)*r-len(R)*len(C))