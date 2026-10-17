n = int(input())
l = list(map(int, input().split()))

ans = []
mini = 1000

for i in range(1,n):
    if abs(l[i]-l[i-1]) < mini:
        mini = abs(l[i]-l[i-1])
        ans = [i-1, i]

if abs(l[0] - l[-1]) < mini:
    ans = [0,n-1]

print(ans[0]+1, ans[1]+1)