n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

vt = [[0 for _ in range(m)] for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def bfs():
    ch = 0
    while q:
        r, c = q.popleft()
        
        if r == n-1 and c == m-1:
            ch = 1
            break
        rc = vt[r][c]
        for d in range(4):
            x = r+dr[d]; y = c+dc[d]
            if 0<=x<n and 0<=y<m:
                if vt[x][y] == 0 and a[x][y] == 1:
                    vt[x][y] = rc+1
                    q.append((x, y))

    return ch
q = deque([(0, 0)])
vt[0][0] = 0
ch = bfs()

if ch:
    print(vt[n-1][m-1])
else:
    print(-1)