n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
c = [int(input()) for _ in range(m)]

# Please write your code here.

def down():
    global g
    for i in range(n):
        tmp = [0 for _ in range(n)]
        n_id = 0
        for j in range(n-1, -1, -1):
            if g[j][i]:
                tmp[n_id] = g[j][i]
                n_id += 1
        for j in range(n):
            g[n-j-1][i] = tmp[j]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def top(i):
    TOP = n-1
    for j in range(n):
        if g[j][i] != 0:
            TOP = j
            break
    return TOP

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bomb(x, y, a):
    global g
    g[x][y] = 0

    for i in range(1, a):
        for d in range(4):
            if in_range(x+dr[d]*i, y+dc[d]*i):
                g[x+dr[d]*i][y+dc[d]*i] = 0
    down()

for i in range(m):
    y = c[i]-1
    x = top(y)
    bomb(x, y, g[x][y])

for i in g:
    print(*i)
