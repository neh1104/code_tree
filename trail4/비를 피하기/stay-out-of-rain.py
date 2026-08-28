n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs():

    while q:
        r, c  = q.popleft()
        if grid[r][c] == 3:
            return r, c
        dist = vt[r][c]

        for d in range(4):
            x = r+dr[d]; y = c+dc[d]
            if 0<=x<n and 0<=y<n and vt[x][y] == -1 and grid[x][y] != 1:
                vt[x][y] = dist+1
                q.append((x, y))

    return -1, -1

result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            vt = [[-1 for _ in range(n)] for _ in range(n)]
            q = deque([(i, j)]); vt[i][j] = 0
            x, y = bfs()
            if x == -1:
                result[i][j] = -1
            else:
                result[i][j] = vt[x][y]

for row in result:
    print(*row)