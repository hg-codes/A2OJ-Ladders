y1 = int(input())

while True:
    y1 += 1
    a,b,c,d = map(int, str(y1))
    if a != b and a != c and a != d and b != c and b != d and c != d:
        print(y1)
        break