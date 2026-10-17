n,k = map(int, input().split())
l = list(map(int, input().split()))

if all(l[num] == l[k-1] for num in range(k-1,n)):
    count = 0
    for i in range(n):
        if l[i] != l[k-1]:
            count = i+1
    print(count)
else:
    print(-1)