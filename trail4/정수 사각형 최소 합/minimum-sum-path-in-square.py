n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

memo = [[0 for _ in range(n)] for _ in range(n)]
memo[0][n-1] = grid[0][n-1]

for i in range(1, n):
    memo[i][n-1] = grid[i][n-1]+memo[i-1][n-1]
    memo[0][n-1-i] = grid[0][n-1-i]+memo[0][n-i]

for i in range(1, n):
    for j in range(n-2, -1, -1):
        memo[i][j] = min(memo[i-1][j], memo[i][j+1])+grid[i][j]

print(memo[n-1][0])
