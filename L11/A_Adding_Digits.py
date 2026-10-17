# a, b, n = map(int, input().split())

# r = a % b
# ans = str(a)

# for _ in range(n):
#     for d in range(10):
#         if (r * 10 + d) % b == 0:
#             r = (r * 10 + d) % b
#             ans += str(d)
#             break
#     else:
#         print(-1)
#         break
# else:
#     print(ans)

a, b, n = map(int, input().split())
for d in range(10):
    if (a * 10 + d) % b == 0:
        print(a * 10 + d, end='')
        print('0' * (n - 1))
        break
else:
    print(-1)