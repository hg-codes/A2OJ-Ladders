def solve():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()

    print(sum(abs(l[i]-i-1) for i in range(n)))

solve()