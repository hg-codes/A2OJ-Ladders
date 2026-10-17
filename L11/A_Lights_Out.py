matrix = [list(map(int, input().split())) for _ in range(3)]
ans = [[1]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        sum = matrix[i][j]
        if i-1 >= 0:
            sum += matrix[i-1][j]
        if i+1 <= 2:
            sum += matrix[i+1][j]
        if j-1 >= 0:
            sum += matrix[i][j-1]
        if j+1 <= 2:
            sum += matrix[i][j+1]
        
        if sum % 2 == 1:
            ans[i][j] = 0
        
for i in range(3):
    for j in range(3):
        print(ans[i][j], end="")
    print()