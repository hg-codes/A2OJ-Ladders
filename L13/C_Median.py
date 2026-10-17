from bisect import bisect_left, bisect_right

n,x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
flag = False

if x not in a:
    a.append(x)
    ans += 1
    n += 1
    flag = True

a.sort()
med = (n+1)//2 - 1
fo = bisect_left(a,x)
lo = bisect_right(a,x)-1

if fo <= med <= lo:
    ans = (1 if flag else 0)
elif lo < med:
    ans += 2*(med-lo)
    if n%2:
        ans -= 1
elif med < fo:
    ans += 2*(fo-med)
    if not n%2:
        ans -= 1

print(ans)