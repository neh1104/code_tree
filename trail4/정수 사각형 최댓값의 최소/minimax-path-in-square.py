n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

vt = [[-1 for _ in range(n)] for _ in range(n)]
vt[0][0] = grid[0][0]

for i in range(1, n):
    vt[i][0] = max(vt[i-1][0], grid[i][0])
    vt[0][i] = max(vt[0][i-1], grid[0][i])

for i in range(1, n):
    for j in range(1, n):
        
        vt[i][j] = max(min(vt[i-1][j], vt[i][j-1]), grid[i][j])

print(vt[n-1][n-1])