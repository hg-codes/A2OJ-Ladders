n,a,b = map(int, input().split())

count = 0 
for i in range(a+1,n+1):
    if n-i <= b:
        count += 1 

print(count)