import sys

def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    d1 = [0]*(2*n-1)
    d2 = [0]*(2*n-1)

    for i in range(n):
        for j in range(n):
            d1[i+j] += a[i][j]
            d2[i-j+n-1] += a[i][j]

    ans1,ans2 = 0,0
    x1,y1,x2,y2 = 1,1,1,2

    for i in range(n):
        for j in range(n):
            d = d1[i+j] + d2[i-j+n-1] - a[i][j]
            if (i+j)&1:
                if d>ans1:
                    ans1 = d
                    x1,y1 = i+1,j+1
            else:
                if d>ans2:
                    ans2 = d
                    x2,y2 = i+1,j+1

    print(ans1+ans2)
    print(x1,y1,x2,y2)

if __name__ == '__main__':
    main()