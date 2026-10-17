s = input()

freq = [0]*26
for c in s:
    freq[ord(c)-ord('a')] += 1

odd = sum(f%2 == 1 for f in freq)

if odd == 0 or odd%2 == 1:
    print("First")
else:
    print("Second")