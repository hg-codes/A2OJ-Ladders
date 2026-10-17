s = input().split("WUB")

while "" in s:
    s.remove("")

for si in s:
    print(si, end=" ")