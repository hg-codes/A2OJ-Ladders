z, o = map(int, input().split())

if z-1 <= o <= 2*(z+1):
    s = '01'*(z-1)
    s += '0'
    o -= z-1

    ob = min(o,z-1)
    l = list(s)
    l[1:2*ob:2] = ['11']*ob
    
    o -= ob
    if o==1:
        l = [*l,'1']
    elif o==2:
        l = [*l,'11']
    elif o==3:
        l = ['1', *l, '11']
    elif o==4:
        l = ['11', *l, '11']

    print("".join(l))

else:
    print(-1)