# s, t = input(), input()
# freq = [0]*60

# for c in s.replace(" ", ""):
#     freq[ord(c)-65] += 1

# for c in t.replace(" ",""):
#     freq[ord(c)-65] -= 1
#     if freq[ord(c)-65] < 0:
#         print("NO")
#         break
# else:
#     print("YES")


from collections import Counter

s, t = input(), input()

if Counter(s.replace(" ", "")) >= Counter(t.replace(" ", "")):
    print("YES")
else:
    print("NO")