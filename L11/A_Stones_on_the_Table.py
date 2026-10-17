n = int(input())
s = list(input())

ans = 0

last = s[0]
for i in range(1,len(s)):
    if s[i] == last:
        ans += 1
    else:
        last = s[i]

print(ans)