n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bounce(d, b):
    if d % 2 == 0:
        if b == 1:
            d = (d+3)%4
        elif b == 2:
            d = (d+1)%4
    else:
        if b == 1:
            d = (d+1)%4
        elif b == 2:
            d = (d+3)%4
    return d

def move(i, j, d):
    t = 1
    while in_range(i, j):
        t += 1
        if a[i][j] != 0:
            d = bounce(d, a[i][j])
        i += dr[d]; j += dc[d]
        #print(i, j)
    #print()
    return t

MAX = 0
for i in range(n):
    t = move(0, i, 0)
    MAX = max(t, MAX)

    t = move(i, 0, 1)
    MAX = max(t, MAX)

    t = move(n-1, i, 2)
    MAX = max(t, MAX)

    t = move(i, n-1, 3)
    MAX = max(t, MAX)

print(MAX)