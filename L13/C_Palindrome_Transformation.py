n,p = map(int, input().split())
s = input()
p -= 1
mn,mx = n,0

count = 0
c_cost = 0

for i in range(n//2):
    if s[i] != s[n-1-i]:
        init, final = map(ord, [s[i], s[n-1-i]])
        if init < final:
            c_cost += min(final-init, init-final+26)
        else:
            c_cost += min(init-final, final-init+26)
        mn = min(mn, i)
        mx = max(mx, i)
    else:
        count += 1

if count == n//2:
    print(0)
    exit()

d_cost = mx-mn
mx1 = n-1-mx
mn1 = n-1-mn

if mn <= p <= mx:
    d_cost += min(mx-p, p-mn)
elif mx1 <= p <= mn1:
    d_cost += min(mn1-p, p-mx1)
elif mx <= p <= mx1:
    d_cost += min(p-mx, mx1-p)
elif p <= mn:
    d_cost += min(n-mn, mn-p)
elif mn1 <= p:
    d_cost += min(p-mn1, 1+mn)

print(c_cost + d_cost)