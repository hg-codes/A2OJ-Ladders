n,m = map(int, input().split())
l = list(map(int, input().split()))

l = [l[i] for i in range(n) if l[i]<0]
l.sort()
l = l[:m]

print(-1*sum(l))