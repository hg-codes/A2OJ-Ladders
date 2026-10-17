s = input().lower()

for x in 'aeiouy':
    s = s.replace(x,'')

s = [ "." + ch for ch in s ]
print("".join(s))