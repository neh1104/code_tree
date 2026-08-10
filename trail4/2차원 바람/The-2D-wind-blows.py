n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def blow(x1, y1, x2, y2):
    x1 -= 1; y1 -= 1
    x2 -= 1; y2 -= 1
    A = a[x1][y2]
    for j in range(y2, y1, -1):
        a[x1][j] = a[x1][j-1]
    
    B = a[x2][y2]
    for i in range(x2, x1, -1):
        a[i][y2] = a[i-1][y2]
    a[x1+1][y2] = A

    C = a[x2][y1]
    for j in range(y1, y2):
        a[x2][j] = a[x2][j+1]
    a[x2][y2-1] = B

    for i in range(x1, x2):
        a[i][y1] = a[i+1][y1]
    a[x2-1][y1] = C

## a 평균값으로 정리
def ABS(i, j):
    n = 1; sum = a[i][j]
    if in_range(i-1, j):
        n+=1
        sum += a[i-1][j]
    if in_range(i, j+1):
        n+=1
        sum += a[i][j+1]
    if in_range(i+1, j):
        n+=1
        sum += a[i+1][j]
    if in_range(i, j-1):
        n+=1
        sum += a[i][j-1]
    abs = sum // n
    return abs

def gkq(x1, y1, x2, y2):
    x1 -= 1; y1-=1; x2-=1;y2-=1
    ls = []
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            ls.append(ABS(i, j))
    #print(ls)
    k = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            a[i][j] = ls[k]
            k+=1

for x1, y1, x2, y2 in winds:
    blow(x1, y1, x2, y2)
    gkq(x1, y1, x2, y2)

for i in a:
    print(*i)