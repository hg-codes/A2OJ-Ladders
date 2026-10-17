chess = [input() for _ in range(8)]

for ro in chess:
    if ro == 'BWBWBWBW' or ro == 'WBWBWBWB':
        continue
    else:
        print("NO")
        break
else:
    print("YES")