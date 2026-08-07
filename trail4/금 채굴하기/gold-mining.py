n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
MAXK = n if n%2 == 0 else n-1

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def diamond(i, j, k):
    sum = 0
    for x in range(-k, k+1):
        for y in range(-k+abs(x), k-abs(x)+1):
            #print(i+x, j+y)
            if in_range(i+x, j+y):
                sum += g[i+x][j+y]
    #print(i, j, sum, k)
    return sum

MAX = 0
for k in range(0, MAXK+1):
    for i in range(n):
        for j in range(n):
            cnt = diamond(i, j, k)
            if cnt * m - (k**2+(k+1)**2) >= 0:
                MAX = max(MAX, cnt)

print(MAX)