n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

from collections import deque

vt = [[0 for _ in range(n)] for _ in range(n)]
def in_range(x, y):
    return 0<=x<n and 0<=y<n and vt[x][y] == 0 and grid[x][y] == 0

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs():
    cnt = 1
    
    while q:
        r, c = q.popleft()
        #print(r, c)
        for d in range(4):
            x = r+dr[d]; y = c+dc[d]
            if in_range(x, y):
                q.append((x, y))
                vt[x][y] = 1
                cnt += 1
    return cnt
s = 0
for i in range(k):
    r, c = points[i]
    if vt[r-1][c-1] == 1:
        continue
    vt[r-1][c-1] = 1
    q = deque([(r-1, c-1)])
    s += bfs()    
print(s)