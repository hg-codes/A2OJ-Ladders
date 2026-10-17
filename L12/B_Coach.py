n,m = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(m)]

teams = []
for a,b in q:
    for t in teams:
        if a in t or b in t:
            t.update({a,b})
            break
    else:
        teams.append({a,b})

for s in range(1,n + 1):
    for i in range(len(teams)):
        if s in teams[i]:
            break
    else:
        teams.append({s})

one, two, three = [], [], []

for team in teams:
    if len(team) == 1:
        one.append(list(team)[0])
    elif len(team) == 2:
        two.append(list(team))
    elif len(team) == 3:
        three.append(list(team))
    else:
        print(-1)
        exit()

if len(two) > len(one):
    print(-1)
    exit()

for a, b in two:
    print(a, b, one.pop())

while len(one) >= 3:
    print(one.pop(), one.pop(), one.pop())

for t in three:
    print(*t)