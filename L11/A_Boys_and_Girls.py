with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())

# if n > m:
#     ans = "BG" * m + "B" * (n - m)
# else:
#     ans = "GB" * n + "G" * (m - n)

ans = ""
a = min(n,m)

if n>m:
    ans += 'BG'*a
    ans += 'B'*(n-m)
else:
    ans += 'GB'*a
    ans += 'G'*(m-n)
    
with open("output.txt", "w") as f:
    f.write(ans + "\n")