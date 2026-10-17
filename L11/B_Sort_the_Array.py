def solve():
    n = int(input())
    l = list(map(int, input().split()))
    s = sorted(l)

    if l==s: print("yes\n1 1"); return

    left,right = -1,-1
    for i in range(1,n):
        if l[i-1]>l[i]:
            if left==-1: left = i-1
            right = i
    
    l= l[:left]+l[left:right+1][::-1]+l[right+1:]
    print("yes" if l==s else "no")
    if l==s: print(left+1,right+1)

solve()