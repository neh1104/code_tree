R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
color = grid[0][0]
cnt = 0
if grid[R-1][C-1] != color:
    for i in range(1, R-2):
        for j in range(1, C-2):
            if grid[i][j] != color:
                for i2 in range(i+1, R-1):
                    for j2 in range(j+1, C-1):
                        if grid[i2][j2] == color:
                            cnt += 1

print(cnt)