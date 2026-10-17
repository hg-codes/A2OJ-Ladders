n,k = map(int, input().split())
s = list(input())

if n == 1:
    print(0)
    print(*s)
    
elif k == 2:
    a1 = ("BA" * ((n + 1) // 2))[:n]
    a2 = ("AB" * ((n + 1) // 2))[:n]

    d1 = sum(s[i] != a1[i] for i in range(n))
    d2 = sum(s[i] != a2[i] for i in range(n))

    if d1 < d2:
        print(d1)
        print(a1)
    else:
        print(d2)
        print(a2)

else:
    count = 0
    for i in range(1, n):
            if s[i] == s[i - 1]:
                for c in "ABC":
                    if c != s[i - 1] and (i == n - 1 or c != s[i + 1]):
                        s[i] = c
                        count += 1
                        break

    print(count)
    print("".join(s))