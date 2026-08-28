n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
from collections import deque

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]
vt = [[-1 for _ in range(n)] for _ in range(n)]

def bfs():

    while q:
        r, c = q.popleft()

        if (r, c) == (r2-1, c2-1):
            break
        
        rc = vt[r][c]

        for d in range(8):
            x = r+dr[d]; y = c+dc[d]
            if 0<=x<n and 0<=y<n and vt[x][y] == -1:
                vt[x][y] = rc+1
                q.append((x, y))

q = deque([(r1-1, c1-1)])
vt[r1-1][c1-1] = 0
bfs()
print(vt[r2-1][c2-1])
