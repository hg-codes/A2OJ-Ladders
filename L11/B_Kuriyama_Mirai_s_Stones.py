from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

m = int(input())
queries = [list(map(int,input().split())) for i in range(m)]

p = [0, *accumulate(a)]
q = [0, *accumulate(sorted(a))]

for [t,l,r] in queries:
        print((p if t == 1 else q)[r] - (p if t == 1 else q)[l-1])