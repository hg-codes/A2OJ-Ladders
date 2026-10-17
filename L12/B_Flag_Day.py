n,m=map(int,input().split())
ans=[0]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())

    if ans[a]:
        x=ans[a]
        ans[b],ans[c]=(x%3)+1,(x+1)%3+1
    elif ans[b]:
        x=ans[b]
        ans[a],ans[c]=(x%3)+1,(x+1)%3+1
    elif ans[c]:
        x=ans[c]
        ans[a],ans[b]=(x%3)+1,(x+1)%3+1
    else:
        ans[a],ans[b],ans[c]=1,2,3

print(*ans[1:])