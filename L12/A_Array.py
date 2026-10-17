n = int(input())
l = list(map(int,input().split()))

a1=[x for x in l if x<0]
a2=[x for x in l if x>0]
a3=[x for x in l if x==0]

if not a2:
    a2 = a1[:2]
    a1 = a1[2:]

if len(a1)%2==0:
    a3.append(a1[0])
    a1 = a1[1:]

print(len(a1), *a1)
print(len(a2), *a2)
print(len(a3), *a3)