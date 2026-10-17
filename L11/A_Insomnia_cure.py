k,l,m,n,d = [int(input()) for _ in range(5)]
print(sum(i%k==0 or i%l==0 or i%m==0 or i%n==0 for i in range(1,d+1)))