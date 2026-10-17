s = input()

s = s.replace('144',' ')
s = s.replace('14',' ')
s = s.replace('1',' ')
s = s.replace(' ','')

if len(s) > 0:
    print("NO")
else:
    print("YES")