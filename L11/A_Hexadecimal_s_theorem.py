n = int(input())

if n == 0:
    print(0,0,0)
elif n ==1:
    print(0,0,1)
else:
    l = [0,1]

    for i in range(2,50):
        l.append(l[i-1]+l[i-2])

    idx = l.index(n)

    print(0,l[idx-1],l[idx-2])