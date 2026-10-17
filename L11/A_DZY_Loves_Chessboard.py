n,m = map(int,input().split())
mat = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        t = i+j
        if mat[i][j] == '.':
            if t%2==0:
                mat[i][j] = 'B'
            else:
                mat[i][j] = 'W'

for row in mat:
    for ch in row:
        print(ch, end = '')
    print()