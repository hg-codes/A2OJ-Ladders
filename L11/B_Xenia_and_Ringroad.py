n,m = map(int, input().split())
l = list(map(int, input().split()))

sum = l[0]-1

for i in range(1,m):
    if l[i] >= l[i-1]:
        sum += l[i]-l[i-1]
    else:
        sum += n+l[i]-l[i-1]

print(sum)