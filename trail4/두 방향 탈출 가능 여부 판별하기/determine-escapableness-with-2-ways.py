n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ch = 0

def can_go(x, y):
    return 0<=x<n and 0<=y<m and grid[x][y] != 0

dr = [1, 0]
dc = [0, 1]
def dfs(r, c):
    global ch
    if ch:
        return

    if r == n-1 and c == m-1:
        ch = 1
        return
    
    grid[r][c] = 0

    for dx, dy in zip(dr, dc):
        x = r+dx; y = c+dy
        if can_go(x, y):
            dfs(x, y)

dfs(0, 0)
print(ch)