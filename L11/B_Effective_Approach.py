n = int(input())
l = list(map(int,input().split()))

m = int(input())
q = list(map(int,input().split()))

l = [(l[i],i) for i in range(n)]
l.sort()

a,b = 0,0

for i in range(m):
    itr = l[q[i]-1][1] + 1
    a += itr
    b += n+1-itr
    
print(a,b)
