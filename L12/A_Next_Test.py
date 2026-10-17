n = int(input())
l = list(map(int, input().split()))
l = [0, *l]
l.sort()

for i in range(n+1):
    if l[i]!=i:
        print(i)
        break
else:
    print(l[-1]+1)