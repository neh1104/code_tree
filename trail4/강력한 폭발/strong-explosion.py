n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ls = [[0 for _ in range(n)] for _ in range(n)]
b_idx = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            b_idx.append((i, j))

b_n = len(b_idx)
b_ls = [[(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
        [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)], 
        [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

MAX = 0
def howMany(curr):
    global MAX
    if curr == b_n:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ls[i][j] > 0:
                    cnt += 1
        MAX = max(MAX, cnt)

        return

    i, j = b_idx[curr]
    for x in range(3):
        for y in range(5):
            dr, dc = b_ls[x][y]
            if in_range(i+dr, j+dc):
                ls[i+dr][j+dc] += 1
        howMany(curr+1)
        for y in range(5):
            dr, dc = b_ls[x][y]
            if in_range(i+dr, j+dc):
                ls[i+dr][j+dc] -= 1
howMany(0)
print(MAX)