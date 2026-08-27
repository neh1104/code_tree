n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_k = 0
for i in range(n):
    for j in range(m):
        max_k = max(max_k, grid[i][j])

def in_range(x, y):
    return 0<=x<n and 0<=y<m and grid[x][y] > k and vt[x][y] == 1

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def dfs(r, c):
    global s
    vt[r][c] = 0

    for d in range(4):
        x = r+dr[d]; y = c+dc[d]
        if in_range(x, y):
            dfs(x, y)

max_s = 0; mk = max_k
for k in range(max_k-1, 0, -1):
    s = 0
    vt = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if in_range(i, j):
                dfs(i, j)
                s += 1
    
    if max_s <= s:
        max_s = s
        mk = k
        
    
print(mk, max_s)