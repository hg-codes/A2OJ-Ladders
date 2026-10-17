MOD = 10**9 + 7
n = int(input())

# A = B = C = 0
# D = 1
# for i in range(n):
#     D,A,B,C = A+B+C, B+C+D, A+C+D, A+B+D
#     D,A,B,C = D%MOD, A%MOD, B%MOD, C%MOD

# A = 0
# D = 1
# for i in range(n):
#     D,A = 3*A, 2*A+D
#     D,A = D%MOD, A%MOD
# print(D)

# Dn = 3An-1
# An = 2An-1 + Dn-1
# Dn = 2Dn-1 + 3Dn-2

# [d,a] = [[3,0][2,1]][a,d]

def matmul(A, B):
    C = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= MOD
    return C

A = [[0, 3], [1, 2]]
R = [[1, 0], [0, 1]]

while n:
    if n & 1:
        R = matmul(R, A)
    A = matmul(A, A)
    n >>= 1

print(R[0][0])