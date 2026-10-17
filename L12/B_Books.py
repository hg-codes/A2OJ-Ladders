n,t = map(int, input().split())
a = list(map(int, input().split()))

i=j=books=ans=0
while i<n:
    while i<n and t >= a[i]:
        t -= a[i]
        books += 1
        i += 1
    ans = max(ans, books)
    while i<n and t < a[i]:
        t += a[j]
        j += 1
        books -= 1

print(ans)