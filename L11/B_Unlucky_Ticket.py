n = int(input())
s = input()

a1, a2 = sorted(s[:n]),sorted(s[n:])

if all(x < y for x,y in zip(a1,a2)) or all(x > y for x,y in zip(a1,a2)):
    print("YES")
else:
    print("NO")