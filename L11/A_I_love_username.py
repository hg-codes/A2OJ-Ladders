n = int(input())
l = list(map(int, input().split()))

maxi = mini = l[0]
ans = 0

for i in range(1,n):
    if l[i] > maxi:
        maxi = l[i]
        ans += 1

    if l[i] < mini:
        mini = l[i]
        ans += 1

print(ans)