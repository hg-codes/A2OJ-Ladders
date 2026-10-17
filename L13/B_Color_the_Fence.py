v = int(input())
a = list(map(int, input().split()))

x = min(a)
d = 0
for i,num in enumerate(a):
    if num == x:
        d = i+1

length = v // x

if length == 0:
    print(-1)
else:
    ans = [d] * length
    rem = v - length * x

    for i in range(length):
        for digit in range(9, d, -1):
            extra = a[digit - 1] - x

            if extra <= rem:
                ans[i] = digit
                rem -= extra
                break

    ans = map(str, ans)
    print("".join(ans))