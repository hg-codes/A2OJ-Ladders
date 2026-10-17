n,m = map(int, input().split())
a = list(map(int, input().split()))
q = [list(map(int, input().split())) for _ in range(m)]
mask = [0]*200005

for l,r in q:
    mask[l] += 1
    mask[r+1] -= 1

for i in range(1,len(mask)):
    mask[i] += mask[i-1]

mask.sort(reverse=True)
a.sort(reverse=True)
s = sum(x*y for x,y in zip(a,mask))
print(s)