a, b = map(list, (input(), input()))

ans = [str(int(a[i])^int(b[i])) for i in range(len(a))]
print("".join(ans))