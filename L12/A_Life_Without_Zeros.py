a=input()
b=input()
c=str(int(a)+int(b))
print("YES" if int(a.replace('0',''))+int(b.replace('0',''))==int(c.replace('0','')) else "NO")