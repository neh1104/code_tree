n, r, c = map(int, input().split())
r-=1; c-=1
a = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

MAX_NUM = a[r][c]
ls = [MAX_NUM]
while True:
    ch = 1
    for d in range(4):
        x = r+dr[d]; y = c+dc[d]
        if in_range(x, y) and a[x][y] > MAX_NUM:
            MAX_NUM = a[x][y]
            r = x; c = y
            ch = 0
            break
    if ch:
        break
    ls.append(MAX_NUM)

print(*ls)