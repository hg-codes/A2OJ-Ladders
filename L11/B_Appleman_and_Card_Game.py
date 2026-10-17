from collections import Counter

n,k = map(int,input().split())
l = sorted(Counter(input()).values(),reverse=True)

su = 0
for x in l:
    t = min(x,k)
    su += t*t
    k -= t
    if not k: break

print(su)