n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()

count = n
small = n//2 - 1
large = n-1

for s in range(small,-1,-1):
    if large > small and 2*l[s] <= l[large]:
        count -= 1
        large -= 1

print(count)