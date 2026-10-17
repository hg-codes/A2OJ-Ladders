x,y = map(int,input().split())
n = int(input())
a=[x-y,x,y,y-x,-x,-y]
print(a[n%6]%1000000007)