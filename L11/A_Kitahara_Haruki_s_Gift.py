n = int(input())
l = list(map(int, input().split()))

a = l.count(100)
b = l.count(200)

if (a%2==0 and b%2==0) or  (a>0 and a%2==0 and b%2==1):
    print("YES")
else:
    print("NO")