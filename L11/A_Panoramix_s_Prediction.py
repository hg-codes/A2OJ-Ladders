import sys

n,m = map(int, input().split())

if n >= m:
    print("NO")
    sys.exit(0)

if n == 2 and m == 3:
    print("YES")
    sys.exit(0)

if n == 2 and m == 4:
    print("NO")
    sys.exit(0)


ans = n
while True:
    ans += 2
    flag = True
    for i in range(2, n):
        if ans % i == 0:
            flag = False
            break
    
    if flag:
        break

if m == ans:
    print("YES")
else:
    print("NO")