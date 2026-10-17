n, k = map(int, input().split())
p = list(map(int, input().split()))

psum = [0] * (n + 1)
for i in range(n):
    psum[i + 1] = psum[i] + p[i]

# sum of every segment of length k
seg = [0] * (n - k + 1)
for i in range(n - k + 1):
    seg[i] = psum[i + k] - psum[i]

# best[i] = best segment among positions 0...i
# store (sum, starting_position)
best = [None] * len(seg)
best[0] = (seg[0], 0)

for i in range(1, len(seg)):
    if seg[i] > best[i - 1][0]:
        best[i] = (seg[i], i)
    else:
        best[i] = best[i - 1]

ans = ans_a = ans_b = -1
for b in range(k, len(seg)):
    # first segment must end before second segment starts
    a_sum, a = best[b - k]
    total = a_sum + seg[b]
    if total > ans:
        ans = total
        ans_a = a
        ans_b = b

print(ans_a + 1, ans_b + 1)