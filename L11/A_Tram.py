n = int(input())

maxi = 0
cap = 0
for i in range(n):
    a,b = map(int, input().split())
    cap += b-a
    maxi = max(maxi,cap)

print(maxi)