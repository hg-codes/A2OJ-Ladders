from bisect import bisect_right

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = sorted(map(int, input().split()))

candidates = sorted(set(a+b))
best_a, best_b = 3*n, 3*m

for d in candidates:
    score_a = 3 * n - bisect_right(a, d)
    score_b = 3 * m - bisect_right(b, d)

    if (score_a - score_b, score_a) > (best_a - best_b, best_a):
        best_a, best_b = score_a, score_b

print(f"{best_a}:{best_b}")