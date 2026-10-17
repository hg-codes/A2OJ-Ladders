def solve():
    N = 10**6
    isPrime = [True] * (N + 1)
    isPrime[0] = isPrime[1] = False

    p = 2
    while p * p <= N:
        if isPrime[p]:
            isPrime[p*p::p] = [False] * len(isPrime[p*p::p])
        p += 1
        
    n = int(input())
    l = list(map(int,input().split()))

    for num in l:
        p = int(num**0.5)
        if p*p == num and isPrime[p]:
            print("YES")
        else:
            print("NO")

solve()