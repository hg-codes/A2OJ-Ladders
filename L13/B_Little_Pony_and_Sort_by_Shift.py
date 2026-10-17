n = int(input())
a = list(map(int, input().split()))
idx = -1

for i in range(n - 1):
    if a[i] > a[i + 1]:
        if idx != -1:
            print(-1)
            exit()
        idx = i

if idx == -1:
    print(0)
elif a[-1] <= a[0]:
    print(n - idx - 1)
else:
    print(-1)