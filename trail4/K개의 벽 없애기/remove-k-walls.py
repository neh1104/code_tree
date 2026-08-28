n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.
wall = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            wall.append((i, j))
l = len(wall)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

remove = []; MIN = 10000
def dfs(curr, d):
    global MIN
    if d == k:
        b = bfs(remove)
        if MIN > b:
            MIN = b
        return
    if curr == l:
        return

    remove.append(wall[curr])
    dfs(curr+1, d+1)
    remove.pop()

    dfs(curr+1, d)

from collections import deque

def bfs(rm):
    vt = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque([(r1, c1)])
    vt[r1][c1] = 0

    while q:
        r, c = q.popleft()

        if r == r2 and c == c2:
            return vt[r][c]
        dist = vt[r][c]

        for d in range(4):
            x = r+dr[d]; y = c+dc[d]
            if 0<=x<n and 0<=y<n and vt[x][y] == -1:
                if grid[x][y] == 0 or (x, y) in rm:
                    vt[x][y] = dist+1
                    q.append((x, y))
    return 10000

dfs(0, 0)
print(MIN if MIN != 10000 else -1)