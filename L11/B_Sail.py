t, s1, s2, e1, e2 = map(int, input().split())
st = input()

d = [max(0, e1-s1), max(0, s1-e1), max(0, e2-s2), max(0, s2-e2)]
mp = {'E': 0, 'W': 1, 'N': 2, 'S': 3}

for i, x in enumerate(st):
    d[mp[x]] = max(0, d[mp[x]] - 1)
    if sum(d) == 0:
        print(i + 1)
        break
else:
    print(-1)