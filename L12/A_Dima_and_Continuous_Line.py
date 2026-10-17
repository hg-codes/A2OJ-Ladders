def yes(): print("yes")
def no(): print("no")

def intersect(a,b,c,d):
    a,b = min(a,b), max(a,b)
    c,d = min(c,d), max(c,d)
    return a<c<b<d or c<a<d<b

def solve():
    n = int(input())
    l = list(map(int, input().split()))

    for i in range(n-1):
        for j in range(i+1,n-1):
            if intersect(l[i], l[i+1], l[j], l[j+1]):
                yes()
                return
            
    no()

solve()