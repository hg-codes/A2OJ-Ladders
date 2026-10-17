n = int(input())
exams = [list(map(int, input().split())) for _ in range(n)]
exams.sort()

last = 0
for a, b in exams:
    if b >= last:
        last = b
    else:
        last = a

print(last)