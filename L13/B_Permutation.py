n = int(input())
a = {x for x in map(int, input().split()) if x <= n}

print(n-len(a))