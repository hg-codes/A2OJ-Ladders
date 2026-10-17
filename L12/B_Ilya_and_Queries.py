from itertools import accumulate
s = list(input())
m = int(input())

a=[0]+[s[i]==s[i+1] for i in range(len(s)-1)]
a=list(accumulate(a))

ans=[None]*m
for i in range(m):
    l,r=map(int,input().split())
    ans[i] = str(a[r-1]-a[l-1])

print('\n'.join(ans))