n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

memo = [[0 for _ in range(n)] for _ in range(n)]
memo[0][0] = grid[0][0]
for i in range(1, n):
    memo[0][i] = memo[0][i-1] if memo[0][i-1] < grid[0][i] else grid[0][i]
    memo[i][0] = memo[i-1][0] if memo[i-1][0] < grid[i][0] else grid[i][0]


for i in range(1, n):
    for j in range(1, n):
        memo[i][j] = min(max(memo[i-1][j], memo[i][j-1]), grid[i][j])

#print(*memo, sep = '\n')
print(memo[n-1][n-1])