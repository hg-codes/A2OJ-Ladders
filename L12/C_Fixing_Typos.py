s = input()
ans = []
i = 0

while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1

    cnt = min(2, j - i)
    if ans and len(ans[-1]) == 2:
        cnt = 1

    ans.append(s[i] * cnt)
    i = j

print("".join(ans))