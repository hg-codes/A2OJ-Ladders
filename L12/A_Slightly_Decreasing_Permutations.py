n,k = map(int, input().split())

a = [i for i in range(1,n+1)]
a = a[-1:n-k-1:-1] + a[:n-k]
print(*a)