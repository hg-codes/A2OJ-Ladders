a,b,c=map(int,input().split())
s=(a+b+c)//2
x,y,z=s-c,s-a,s-b

if min(x,y,z)>=0 and 2*(x+y+z)==a+b+c:
    print(x,y,z)
else:
    print("Impossible")