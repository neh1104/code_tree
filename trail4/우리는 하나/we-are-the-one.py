n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def in_range(x, y):
    return 0<=x<n and 0<=y<n and vt[x][y] == 0

vt = [[0 for _ in range(n)] for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs():
    cnt = 1
    while q:
        r, c = q.popleft()
        rc = grid[r][c]
        for i in range(4):
            x = r+dr[i]; y = c+dc[i]
            
            if in_range(x, y) and u <= abs(rc-grid[x][y]) <= d:
                vt[x][y] = 1
                q.append((x, y))
                cnt += 1
    return cnt

ls = []
for i in range(n):
    for j in range(n):
        if vt[i][j] == 0:
            vt[i][j] = 1
            q = deque([(i, j)])
            ls.append(bfs())
#print(ls)

ls.sort(key = lambda x: -x)
s = 0
k = k if len(ls) > k else len(ls)
for i in range(k):
    s += ls[i]
print(s)