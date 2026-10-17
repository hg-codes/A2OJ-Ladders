s = input()
uc,lc = 0,0

for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        lc += 1
    else:
        uc += 1

if lc >= uc:
    print(s.lower())
else:
    print(s.upper())