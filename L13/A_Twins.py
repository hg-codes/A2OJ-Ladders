n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
sa = coins = 0
sb = sum(a)

for c in a:
    sa += c
    sb -= c
    coins += 1
    if sa>sb:
        break

print(coins)