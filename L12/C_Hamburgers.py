s = input()
need = [s.count('B'), s.count('S'), s.count('C')]
available = list(map(int, input().split()))
price = list(map(int, input().split()))
money = int(input())

def can_make(N):
    tot_price = [max(a*N-x, 0)*p for a, x, p in zip(need, available, price)]
    return sum(tot_price) <= money

ans = l = 0
r = 10**18
while l<=r:
    m = (l+r)//2
    if can_make(m):
        ans = m
        l = m+1
    else:
        r = m-1

print(ans)