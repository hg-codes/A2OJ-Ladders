k = int(input())
s = input()
ans = 0

if k == 0:
    z = 0
    for c in s:
        if c == '0':
            z += 1
        else:
            ans += z * (z + 1) // 2
            z = 0

    ans += z * (z + 1) // 2
    print(ans)
    exit()

ones = [-1] + [i for i, c in enumerate(s) if c == '1'] + [len(s)]
m = len(ones) - 2

for i in range(1, m - k + 2):
    left = ones[i] - ones[i - 1]
    right = ones[i + k] - ones[i + k - 1]
    ans += left * right

print(ans)