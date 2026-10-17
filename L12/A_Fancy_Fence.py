n = int(input())
l = [int(input()) for _ in range(n)]

for a in l:
    d = 180 - a
    print("YES" if d > 0 and 360 % d == 0 and 360 // d >= 3 else "NO")