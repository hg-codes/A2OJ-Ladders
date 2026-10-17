n,k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

l.sort(key = lambda x: (-x[0],x[1]))

print(l.count(l[k-1]))