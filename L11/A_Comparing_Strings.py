s, t = input(), input()
diff = [(a, b) for a, b in zip(s, t) if a != b]
print("YES" if len(s) == len(t) and len(diff) == 2 and diff[0] == diff[1][::-1] else "NO")