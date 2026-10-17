k = int(input())
s = input()

freq = [s.count(chr(97+i)) for i in range(26)]

flag = True
for f in freq:
    if f%k != 0:
        flag = False
        break

if flag:
    ans = ""
    for i in range(26):
        if freq[i] > 0:
            ans += (chr(97+i)*(freq[i]//k))
    print(ans*k)
else:
    print(-1)