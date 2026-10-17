n,m = map(int, input().split())
l = list(map(int, input().split()))
mx = max(l)

f = (mx//m if mx%m !=0 else mx//m -1)
l = [max(-1,l[i]-f*m) for i in range(n)]

ans = 0
for i in range(n):
    if l[i] > 0:
        ans = i

print(ans+1)