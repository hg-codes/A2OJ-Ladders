def solve():
    a = input()
    b = input()
    
    if len(a) != len(b):
        print("NO")
        return

    ina = (1 if '1' in a else 0)
    inb = (1 if '1' in b else 0)

    if ina == inb:
        print("YES")
    else:
        print("NO")
           

solve()