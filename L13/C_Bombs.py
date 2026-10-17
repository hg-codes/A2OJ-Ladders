def main():
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]

    a.sort(key = lambda x : x[0]**2 + x[1]**2)

    ops = []
    for x, y in a:
        if x:
            ops.append(f"1 {abs(x)} {'R' if x > 0 else 'L'}")
        if y:
            ops.append(f"1 {abs(y)} {'U' if y > 0 else 'D'}")

        ops.append("2")

        if x:
            ops.append(f"1 {abs(x)} {'L' if x > 0 else 'R'}")
        if y:
            ops.append(f"1 {abs(y)} {'D' if y > 0 else 'U'}")

        ops.append("3")

    print(len(ops))
    print("\n".join(ops))

if __name__ == "__main__":
    main()