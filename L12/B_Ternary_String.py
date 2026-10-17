def solve():
    s = input()

    if len(set(s))<3:
        print(0)
        return

    c = [0]*3 
    j=0
    ans = 200000
    for i,x in enumerate(s):
        c[int(x)-1] += 1
        while min(c) > 0:
            ans = min(ans,i-j+1)
            c[int(s[j])-1] -= 1
            j += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()