n,m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

l = [li[1:] for li in l]
money = 0

for i in range(1,m+1):
    nli = []
    for li in l[:]:
        if i in li:
            nli.extend(li)
            l.remove(li)
    if nli:
        l.append(nli)

for li in l[:]:
    if not li:
        money += 1
        l.remove(li)

if len(l):
    print(len(l)-1+money)
else:
    print(money)