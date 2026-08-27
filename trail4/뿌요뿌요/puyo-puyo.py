n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
vt = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n and vt[x][y] == 0

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    global cnt
    vt[r][c] = 1
    cnt += 1
    for d in range(4):
        x = r+dr[d]; y = c+dc[d]
        if in_range(x, y) and grid[x][y] == grid[r][c]:
            dfs(x, y)

b_cnt = 0; MAX = 0
for i in range(n):
    for j in range(n):
        if in_range(i, j):
            cnt = 0
            dfs(i, j)
            if cnt >= 4:
                b_cnt += 1
            MAX = max(MAX, cnt)

print(b_cnt, MAX)