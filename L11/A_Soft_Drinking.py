n,k,l,c,d,p,nl,np = list(map(int, input().split()))

a1 = k*l/(nl*n)
a2 = c*d/n
a3 = p/(np*n)

print(int(min(a1,a2,a3)))