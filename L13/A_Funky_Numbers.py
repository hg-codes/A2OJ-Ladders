from bisect import bisect_left
S = int(input())

ans = []
for k in range(1,44721):
    num = (k*(k+1))//2
    ans.append(num)

for num in ans:
    idx = bisect_left(ans, S-num)
    if idx < len(ans) and ans[idx]==S-num:
        print("YES")
        break
else:
    print("NO")