from bisect import bisect_right
# import sys
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = n
prev = -1

for i,num in enumerate(a):
    if num == prev:
        continue
    
    l_pos = 2*num
    j = bisect_right(a, l_pos)
    ans = min(ans,n-j+i)
    prev = num

print(ans)