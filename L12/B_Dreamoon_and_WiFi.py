ref = input()
s = input()

pos = ref.count('+') - ref.count('-')
p = s.count('+')-s.count('-')
count =s.count('?')

candidates = []
for x in range(1<<count):
    b = f'{x:0{count}b}' if count else ''
    ps = b.count('0')-b.count('1')
    candidates.append(p+ps)

ans = candidates.count(pos)/(1<<count)
print(f'{ans:.12f}')