s = input()

if s[0] != '-':
    print(s)
else:
    s = s[1:]
    n = len(s)    
    s1 = s[:n-1]
    s2 = s[:n-2] + s[n-1]
    print(max(-int(s), -int(s1), -int(s2)))