n = int(input())
l = list(map(int,input().split()))

if sum(l)%2:
    print(sum(x%2 for x in l))
else:
    print(sum(x%2==0 for x in l))