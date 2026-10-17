n = int(input())
l = list(map(int, input().split()))

if any(x in l for x in [5, 7]) or l.count(1) != n//3 or 3 in l and 3 == max(l):
    print(-1)
else:
    t, h, f, s = map(l.count, [2, 3, 4, 6])

    a, b, c = f, 0, h
    t -= f
    s -= h

    if t < 0 or s < 0 or t != s:
        print(-1)
    else:
        b = t
        if a + b + c == n//3:
            print("\n".join(["1 2 4"]*a + ["1 2 6"]*b + ["1 3 6"]*c))
        else:
            print(-1)