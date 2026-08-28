n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

vt = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<m and vt[x][y] == 0

def bfs():
    global cnt
    global how_many
    while q:
        r, c = q.popleft()
        #print(r, c)
        for d in range(4):
            x = r+dr[d]; y = c+dc[d]
            if in_range(x, y):
                if nvt[x][y]:
                    continue
                if a[x][y]:
                    nq.append((x, y))
                    nvt[x][y] = 1
                    how_many += 1
                else:
                    #print(x,y)
                    q.append((x, y))
                    vt[x][y] = 1
                    cnt += 1
                    


cnt = 0; nq = deque([(0, 0)])
time = -1
ls = []
while cnt < n*m:
    q = deque(nq); nq = deque()
    if q == deque([]):
        break
    r, c = q[0]; vt[r][c] = 1; cnt += 1
    nvt = [[0 for _ in range(m)] for _ in range(n)]
    how_many = 0; time += 1

    bfs()
    ls.append(how_many)
    #print(q, nq)
    for i, j in nq:
        a[i][j] = 0
print(time, ls[-2])