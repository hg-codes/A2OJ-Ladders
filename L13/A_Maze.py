n,m,k = map(int, input().split())
maze = [list(input()) for _ in range(n)]

if k == 0:
    for r in maze:
        print("".join(r))
    exit()

stack, ans = [], []

flag = False
for i in range(n):
    for j in range(m):
        if maze[i][j]=='.':
            stack.append((i,j))
            flag = True
            break
    if flag : break

visited = set()

while stack:
    x,y = stack.pop()
    visited.add((x,y))

    for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx = x + i
        ny = y + j
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.' and (nx,ny) not in visited:
            visited.add((nx,ny))
            stack.append((nx,ny))
            ans.append((nx,ny))

for x,y in ans[-k:]:
    maze[x][y] = 'X'

for r in maze:
        print("".join(r))