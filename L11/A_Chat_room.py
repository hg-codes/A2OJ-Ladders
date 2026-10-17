s = input()

for x in 'hello':
    if x in s:
        s = s[s.index(x)+1:]
        if x == 'o':
            print("YES")
    else:
        print("NO")
        break