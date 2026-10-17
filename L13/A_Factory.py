import math
a,m = map(int, input().split())

for _ in range(int(math.log2(m))+1):
    a += a%m
    if a%m==0:
        print("Yes")
        break
else:
    print("No")