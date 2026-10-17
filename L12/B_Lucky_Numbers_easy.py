def lucky_no(d):
    l = []
    for i in range(2**d):
        t = f'{i:0{d}b}'
        if t.count('0') == d//2:
            l.append(t.translate(str.maketrans('01', '47')))
    l = list(map(int, l))
    return l

l = []
for i in range(2,11,2):
    l.extend(lucky_no(i))

n = int(input())
for num in l:
    if num>=n:
        print(num)
        break