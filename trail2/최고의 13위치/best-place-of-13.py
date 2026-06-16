n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
MAX = 0
for i in range(n):
    for j in range(n-2):
        cnt = sum(grid[i][j:j+3])
        MAX = max(MAX, cnt)

print(MAX)