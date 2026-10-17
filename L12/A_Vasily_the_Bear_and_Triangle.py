a,b=map(int,input().split())
s=abs(a)+abs(b)
q=(a<0)*2+(b<0)

print(*[(0,s,s,0),(0,-s,s,0),(-s,0,0,s),(-s,0,0,-s)][q])