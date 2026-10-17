n = int(input())
l = list(map(int,input().split()))

maxi, mini = max(l), min(l)

itr = len(l) - 1 - l[::-1].index(mini)
ITR = l.index(maxi)

sum = n - itr + ITR - (1 if itr>ITR else 2)
print(sum)