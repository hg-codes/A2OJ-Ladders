m,n = map(int, input().split())
a = [0]*(m+1)

# for i in range(1,m+1):
#     a[i] = (i**n - (i-1)**n)*i

# expected = sum(a)/(m**n)
# print(f'{expected:.12f}')
# causing overflow

# alternate approach
for i in range(1,m):
    a[i] = (i/m)**n

expected = m - sum(a)
print(f'{expected:.12f}')