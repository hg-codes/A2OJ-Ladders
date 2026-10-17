n,k = map(int, input().split())
l = list(map(int, input().split()))

neg = [x for x in l if x<0]
pos = [x for x in l if x>=0]
neg_num = len(neg)

if len(neg) >= k:
    pos += [-x for x in neg[:k]]
    neg = neg[k:]
    print(sum(pos) + sum(neg))
else:
    pos += [-x for x in neg]
    if 0 in pos or (k-neg_num)%2==0:
        print(sum(pos))
    else:
        print(sum(pos)-2*min(pos))