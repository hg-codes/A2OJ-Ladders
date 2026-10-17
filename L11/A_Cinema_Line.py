n = int(input())
l = list(map(int, input().split()))
q = h = 0

for x in l:
    if x == 25: q += 1
    elif x == 50 and q: q -= 1;h += 1
    elif x == 100 and (q>2 or (q and h)):
        if q and h: q-=1; h-=1
        else: q-=3
    else: print("NO");break
else: print("YES")