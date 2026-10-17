n = int(input())
l = list(map(int,input().split()))
s = set(l)

limit = (n//2 if n%2==0 else n//2 + 1)

for num in s:
    if l.count(num) > limit:
        print("NO")
        break
else:
    print("YES")