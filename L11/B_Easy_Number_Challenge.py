def solve():
    M = 1073741824
    a,b,c = map(int,input().split())
    m = a*b*c
    d=[0]*(m+1)

    # Count divisors for each number from 1 to MAX_VALUE
    for i in range(1,m+1):
        # for each multiple of i, increment the divisor count
        # [d[i], d[2*i], d[3*i], ..., d[m//i * i]]  = [d[i], d[2*i], d[3*i], ..., d[m//i * i]] + 1
        d[i::i] = [x+1 for x in d[i::i]]

    ans=0
    for i in range(1,a+1):
        for j in range(1,b+1):
            ij = i*j
            for k in range(1,c+1):
                ans+=d[ij*k]

    print(ans%M)

solve()


# def divisor(n):
#     p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,73, 79, 83, 89, 97]
#     k = 1
#     for i in p:
#         j = 1
#         if n < i:
#             break
#         while n % i == 0 and n >= i:
#             n /= i
#             j += 1
#         k *= j
#     return k
# def solve():
#     a,b,c=map(int,input().split())
#     ans=0
#     dic = {}
#     for i in range(1,a+1):
#         for j in range(1,b+1):
#             for k in range(1,c+1):
#                 l = i*j*k
#                 if l not in dic:
#                     dic[l] = divisor(l)
#                 ans +=dic[l]
#     print(ans%1073741824)
                
# if __name__ == '__main__':
#     solve()