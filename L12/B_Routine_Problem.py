import math
a, b, c, d = map(int, input().split())
 
if a * d > b * c:
    # screen is wider 
    # mult factor b/d
    num = a * d - b * c
    den = a * d
elif a * d < b * c:
    # screen is taller
    # mult factor a/c
    num = b * c - a * d
    den = b * c
else:
    num = 0
    den = 1
 
g = math.gcd(num, den)
print(f"{num//g}/{den//g}")