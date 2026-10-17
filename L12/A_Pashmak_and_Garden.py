x1,y1,x2,y2=map(int,input().split())

if x1==x2:
    d=abs(y1-y2)
    if abs(x1-d)<1000: print(x1-d,y1,x1-d,y2)
    elif abs(x1+d)<1000: print(x1+d,y1,x1+d,y2)
    else: print(-1)

elif y1==y2:
    d=abs(x1-x2)
    if abs(y1-d)<1000: print(x1,y1-d,x2,y1-d)
    elif abs(y1+d)<1000: print(x1,y1+d,x2,y1+d)
    else: print(-1)

else:
    if abs(x1-x2)!=abs(y1-y2):
        print(-1)
    elif max(abs(x1),abs(x2),abs(y1),abs(y2))>=1000:
        print(-1)
    else:
        print(x1,y2,x2,y1)