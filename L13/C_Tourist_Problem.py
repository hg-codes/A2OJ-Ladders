import math

def frac(num, den):
    g = math.gcd(num, den)
    num = num//g
    den = den//g
    return num, den

n = int(input())
a = list(map(int, input().split()))
a.sort()

num = sum(a)
prefix, Sleft = 0, 0
for i, x in enumerate(a):
    Sleft += i * x - prefix
    prefix += x
num += 2*Sleft

print(*frac(num, n))