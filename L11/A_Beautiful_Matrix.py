matrix = [list(map(int,input().split())) for _ in range(5)]
ans = next(abs(i - 2) + abs(j - 2) for i in range(5) for j in range(5) if matrix[i][j] != 0)
print(ans)