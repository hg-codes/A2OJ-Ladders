n = input()

count = 0
while len(n)!=1:
    tot = 0
    for dig in n:
        tot += int(dig)
    n = str(tot)
    count += 1

print(count)