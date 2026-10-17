def lucky(x):
    l = []
    for i in range(2**x):
        b=f'{i:0{x}b}'
        l.append(int(b.replace('0','4').replace('1','7')))
    return l

l,r=map(int,input().split())

lucky_no=[]
for x in range(1,11):
    lucky_no.extend(lucky(x))

sum=0
for x in lucky_no:
    if x<l:
        continue
    sum+=(min(x,r)-l+1)*x
    l=x+1
    if l>r:
        break

print(sum)