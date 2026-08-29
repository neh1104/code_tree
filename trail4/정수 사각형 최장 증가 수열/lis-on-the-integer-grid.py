n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dp(r, c):
    if memo[r][c] != -1:
        return memo[r][c]
    now = grid[r][c]

    MAX = 1
    for d in range(4):
        x = r + dr[d]
        y = c + dc[d]
        if 0 <= x < n and 0 <= y < n and grid[x][y] > now:
            MAX = max(MAX, dp(x, y) + 1)
    memo[r][c] = MAX
    return memo[r][c]

MAX = 0
memo = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):        
        MAX = max(MAX, dp(i, j))
        #print(*memo, sep = '\n')
        #print()
print(MAX)
