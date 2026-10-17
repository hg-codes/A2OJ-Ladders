n = int(input())

mx = n*n
mn = 1

for _ in range(n):
    for i in range(1,n//2+1):
        print(mn, end = " ")
        mn += 1
    for j in range(1,n//2+1):
        print(mx, end = " ")
        mx -= 1
    print()