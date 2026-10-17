from bisect import bisect_right

n,d = map(int, input().split())
a = list(map(int, input().split()))

def func(n):
    return n*(n+1)//2

def startend(i):
    if a[i+2] > d + a[i]:
        return -1,0
    start = i+2
    end = bisect_right(a,a[i]+d)-1
    return end, start

sum = 0
for i,num in enumerate(a[:-2]):
    k,j = startend(i)
    diff = k-j+1
    sum += func(diff)
print(sum)