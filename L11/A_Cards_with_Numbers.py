with open("input.txt") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

pos = {}

for i, x in enumerate(a, 1):
    if x in pos:
        pos[x].append(i)
    else:
        pos[x] = [i]

with open("output.txt", "w") as f:
    if any(len(v) % 2 for v in pos.values()):
        f.write("-1\n")
    else:
        for v in pos.values():
            for i in range(0, len(v), 2):
                f.write(f"{v[i]} {v[i+1]}\n")