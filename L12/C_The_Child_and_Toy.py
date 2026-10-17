n,m = map(int, input().split())
l = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]

s = sum(min(l[a-1],l[b-1]) for [a,b] in edges)
print(s)