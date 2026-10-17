a, b, c = map(int, input().split())
A = a*b*c
S = 0

for x in (a,b,c):
    S += 4*(A//(x*x))**0.5

print(int(S))