n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

vt = [[-1 for _ in range(m)] for _ in range(n)]
vt[n-1][m-1] = 1
def td(r, c):
    if vt[r][c] != -1:
        return vt[r][c]
    

    now = grid[r][c]
    MAX = 1
    for i in range(r+1, n):
        for j in range(c+1, m):
            if grid[i][j] > now:
                MAX = max(MAX, td(i, j)+1)
    vt[r][c] = MAX

    return MAX

print(td(0, 0))