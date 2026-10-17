n,k = map(int, input().split())
a = list(map(int, input().split()))
freq = [0]*(max(a) +1)
count = 1

i,j = 0,1
freq[a[0]] += 1

while count < k and j < n:
    if freq[a[j]] == 0:
        count += 1
    freq[a[j]] += 1
    j += 1

if count == k:    
    while freq[a[i]] > 1:
        freq[a[i]] -= 1
        i += 1
    print(i+1, j)
else:
    print(-1,-1)