s = input()
sum = 0

for i in range(len(s)):
    if s[i] == '4' or s[i] == '7':
        sum += 1

# now to check if sum is lucky or not
sum = str(sum)

flag = True
for i in range(len(sum)):
    if sum[i] == '4' or sum[i] == '7':
        flag = True
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
