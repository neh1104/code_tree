n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(mr, mc, MAX, start):

    while q:
        r, c = q.popleft()
        
        for d in range(4):
            i = r + dr[d]; j = c+dc[d]
            if not(in_range(i, j)): #범위를 벗어난다면
                continue
            if vt[i][j]: #현재 탐색에서 이미 방문한 곳일때
                continue

            if grid[i][j] >= start: #스타트 값보다 클 때

                continue

            q.append((i, j))
            vt[i][j] = 1  
            #선택
            if grid[i][j] < MAX:
                continue

            if grid[i][j] == MAX and (i <= mr or (i == mr and j < mc)):
                mr = i; mc = j

            if grid[i][j] > MAX:
                MAX = grid[i][j]
                mr = i; mc = j

            
    return mr, mc

r -= 1; c -= 1

for _ in range(k):
    vt = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(r, c)])
    vt[r][c] = 1
    mr = r; mc = c; MAX = 0
    r, c = bfs(mr, mc, MAX, grid[r][c])
    if mr == r and mc == c:
        break

print(r+1, c+1)
    