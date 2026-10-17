n,m = map(int, input().split())
f = set(range(1,n+1))
s = set()

print(n-1)

for _ in range(m):
    s.update(map(int, input().split()))

r = f-s
ref = next(iter(r))

for num in f:
    if ref != num:
        print(ref, num)