n = int(input())
l = list(map(int,input().split()))

if 0 in l:
    s = sum(l)//45
    s = 9*s
    z = l.count(0)
    if(s>0):
        print('5'*s + '0'*z)
    else:
        print(0)
else:
    print("-1")