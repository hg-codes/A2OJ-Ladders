n = int(input())
l = list(map(int, input().split()))
c = sum(l[i]==i for i in range(n))

if c>=n-2:
    print(n)
else:
    for i in range(n):
        if l[i] != i and l[l[i]]==i:
            print(c+2)
            break
    else:
        print(c+1)