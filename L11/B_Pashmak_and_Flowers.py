n = int(input())
l = list(map(int, input().split()))
l.sort()

diff = l[-1]-l[0]
ways = l.count(l[0])*l.count(l[-1])

if diff == 0:
    m = l.count(l[0])
    ways = (m*(m-1))//2

print(diff, ways)
