n = int(input())
l = list(map(int, input().split()))
l.sort()

l = [l[-1]] + l[1:n-1] + [l[0]]
print(*l)