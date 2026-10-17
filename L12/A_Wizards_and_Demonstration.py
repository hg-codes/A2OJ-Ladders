import math
n,x,y = map(int, input().split())

mn = math.ceil(y*n/100)
print(max(0,mn-x))