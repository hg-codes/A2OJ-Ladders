a, b = map(int, input().split())
print(max(a,b)-1, min(a,b))

# vasya has to get min(a,b) points as she can always generate the diff pair since the diff pair ball lasts
# petya simply got a+b-1-min(a,b) i.e max(a,b)-1