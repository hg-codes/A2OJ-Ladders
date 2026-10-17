n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if max(max(a),2*min(a)) < min(b):
    print(max(max(a),2*min(a)))
else:
    print(-1)
