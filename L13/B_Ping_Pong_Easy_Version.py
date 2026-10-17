n = int(input())

intervals = []
adj = []

for _ in range(n):
    q, a, b = map(int, input().split())

    if q == 1:
        idx = len(intervals)
        adj.append([])

        for i, (c, d) in enumerate(intervals):
            if c < a < d or c < b < d:
                adj[idx].append(i)

            if a < c < b or a < d < b:
                adj[i].append(idx)

        intervals.append((a, b))

    else:
        src, dst = a - 1, b - 1
        vis = {src}
        stack = [src]

        while stack and dst not in vis:
            u = stack.pop()

            for v in adj[u]:
                if v not in vis:
                    vis.add(v)
                    stack.append(v)

        print("YES" if dst in vis else "NO")