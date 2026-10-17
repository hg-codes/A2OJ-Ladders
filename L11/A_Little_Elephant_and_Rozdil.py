n = int(input())
l = list(map(int, input().split()))

i1 = l.index(min(l))
i2 = l[::-1].index(min(l))

if i1==n-1-i2:
    print(i1+1)
else:
    print("Still Rozdil")