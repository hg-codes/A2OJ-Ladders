import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = 1 << n
a = list(map(int, input().split()))

tree = [0] * (2 * N)

# Build the leaves
for i in range(N):
    tree[N + i] = a[i]

# Build internal nodes from bottom to top
level = 1
size = N // 2

while size:
    op_or = (level % 2 == 1)

    for i in range(size, 2 * size):
        if op_or:
            tree[i] = tree[2 * i] | tree[2 * i + 1]
        else:
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

    level += 1
    size //= 2

for _ in range(m):
    p, b = map(int, input().split())
    p = N + p - 1
    tree[p] = b

    # Update all ancestors
    while p > 1:
        p //= 2

        # Determine operation from this node's depth
        depth = (p.bit_length() - 1)
        height = n - depth

        if height % 2 == 1:
            tree[p] = tree[2 * p] | tree[2 * p + 1]
        else:
            tree[p] = tree[2 * p] ^ tree[2 * p + 1]

    print(tree[1])