# n = int(input())
# a = [input() for _ in range(n)]

# print(max(set(a), key=a.count))

n = input()

if '0000000' in n or '1111111' in n:
    print("YES")
else:
    print("NO")