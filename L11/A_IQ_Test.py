def solve():
    a = [input() for i in range(4)]

    for i in range(3):
        for j in range(3):
            s = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
            if s.count('#') >= 3 or s.count('.') >= 3:
                print("YES")
                return
    else:
        print("NO")

solve()