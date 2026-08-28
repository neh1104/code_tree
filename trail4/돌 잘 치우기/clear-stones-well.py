n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.
rock = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            rock.append((i, j))

l = len(rock)
d_rock = []; ls = []
def dfs(curr, d):
    global ls
    global d_rock

    if d == m:
        d_rock.append(ls[:])
        return
    if curr == l:
        return

    ls.append(rock[curr])
    dfs(curr+1, d+1)
    ls.pop()

    dfs(curr+1, d)

dfs(0, 0)

from collections import deque

def in_range(x, y):
    return 0<=x<n and 0<=y<n and vt[x][y] == 0 and a[x][y] == 0

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def bfs():
    cnt = 0
    while q:
        r, c = q.popleft()    

        for d in range(4):
            x = r+dr[d]; y = c+dc[d]
            if in_range(x, y):
                q.append((x, y))
                vt[x][y] = 1
                cnt += 1
    return cnt
MAX = 0
for j in range(len(d_rock)):
    a = [row[:] for row in grid]
    for x, y in d_rock[j]:
        a[x][y] = 0
    vt = [[0 for _ in range(n)] for _ in range(n)]
    CNT = 0
    for i in range(k):
        x = r[i]; y = c[i]
        q = deque([(x, y)])
        CNT += bfs()
        if CNT > MAX:
            #print(*a, sep = '\n')
            #print(CNT, MAX)
            #print()
            MAX = CNT

print(MAX)
