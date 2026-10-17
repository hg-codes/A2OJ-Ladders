r,g,b = map(int, input().split())

ans = 0
for m in range(3):
    count = 0
    if min(r,g,b)>=m:
        count = m
        r,g,b = r-m,g-m,b-m
    count += r//3 + g//3 + b//3 + min(r%3, g%3, b%3)
    ans = max(ans, count)

print(ans)