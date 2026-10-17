from itertools import permutations

g = [list(map(int, input().split())) for _ in range(5)]

def f(a, b):
    return g[int(a)-1][int(b)-1] + g[int(b)-1][int(a)-1]

maxi = su = 0

for p in permutations('12345'):
    su = f(p[0],p[1]) + 2 * f(p[2],p[3]) + f(p[1],p[2]) + 2 * f(p[3],p[4])
    maxi = max(maxi,su)

print(maxi)