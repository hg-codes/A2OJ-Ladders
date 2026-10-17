ans = [0]*200001
dig_sum = [0]*200001

def precompute():   
    for i in range(1,200001):
        dig_sum[i] = dig_sum[i//10] + i%10
        ans[i] = dig_sum[i] + ans[i-1]

def solve():
    n = int(input())
    print(ans[n])

t = int(input())
precompute()
for _ in range(t):
    solve() 