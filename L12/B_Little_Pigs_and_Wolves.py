r,c=map(int,input().split())
a=[input() for _ in range(r)]

ans=0
for i in range(r):
    for j in range(c):
        if a[i][j]=='W' and (
            i and a[i-1][j]=='P' or
            i+1<r and a[i+1][j]=='P' or
            j and a[i][j-1]=='P' or
            j+1<c and a[i][j+1]=='P'
        ):
            ans+=1

print(ans)