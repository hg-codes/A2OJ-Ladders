import heapq

n,_ = map(int,input().split())
l = list(map(int,input().split()))
h = [-x for x in l]

heapq.heapify(l)
heapq.heapify(h)

mini = maxi = 0

for _ in range(n):
    ele1 = heapq.heappop(l)
    ele2 = -heapq.heappop(h)
    mini += ele1
    maxi += ele2

    if ele1 > 1:
        heapq.heappush(l,ele1-1)
    if ele2 > 1:
        heapq.heappush(h,1-ele2)

print(maxi, mini)