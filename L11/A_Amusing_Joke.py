a = list(input())
b = list(input())
c = list(input())

s = a + b
s.sort()
c.sort()

if c == s:
    print("YES")
else:
    print("NO")