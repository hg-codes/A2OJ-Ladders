n, r, avg = map(int, input().split())
req = avg * n
q = [list(map(int, input().split()))[::-1] for _ in range(n)]
q.sort()

curr = sum(a for b, a in q)

if curr >= req:
    print(0)
else:
    essay = 0
    for b, a in q:
        gain = min(r - a, req - curr)
        essay += gain * b
        curr += gain

        if curr == req:
            break
    print(essay)