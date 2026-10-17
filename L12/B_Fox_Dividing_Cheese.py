import math

a, b = map(int,input().split())
g = math.gcd(a,b)
a, b = a//g, b//g
op = 0

for x in (2,3,5):
    while a%x==0:
        a //= x; op += 1
    while b%x==0:
        b //= x; op += 1

print(op if a==b==1 else -1)