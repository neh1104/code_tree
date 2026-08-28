n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

q = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i, j))

vt = [[-1 for _ in range(n)] for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for i, j in q:
    vt[i][j] = 0

def bfs():

    while q:    
        r, c = q.popleft()
        
        dist = vt[r][c]

        for d in range(4):
            x = r+dr[d]; y = c+dc[d]
            if 0<=x<n and 0<=y<n and vt[x][y] == -1:
                if grid[x][y] == 1:
                    q.append((x, y))
                    vt[x][y] = dist+1

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and vt[i][j] == -1:
            print(-2, end = ' ')
        else:
            print(vt[i][j], end = ' ')
    print()