s = input()

if '0' in s:
    a = s.index('0')
    s = s[:a] + s[a+1:]
    print(s)
else:
    s = s[:-1]
    print(s)