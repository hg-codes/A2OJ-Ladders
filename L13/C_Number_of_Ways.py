n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)

if n<3: print(0); exit()
if total % 3 != 0: print(0); exit()

target = total//3
a, b = 0,0
sum = 0

arr.pop() # third part should be min of len 1
for num in arr:
    sum += num
    if sum == 2*target:
        a += b
    if sum == target:
        b += 1

print(a)