n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n and grid[x][y] == 1


def choose(r, c):
    global MAX

    grid[r][c] = 0
    MAX += 1


    for d in range(4):
        x = r+dr[d]; y = c+dc[d]
        if in_range(x, y):
            choose(x, y)

ls = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            MAX = 0 
            choose(i, j)
            ls.append(MAX)

print(len(ls))
ls.sort()
print(*ls, sep = '\n')