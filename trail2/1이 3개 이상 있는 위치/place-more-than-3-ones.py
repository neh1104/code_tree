n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x, y):
    return 0<=x<n and 0<=y<n

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
for i in range(n):
    for j in range(n):
        cnt_1 = 0
        for k in range(4):
            x = i+dx[k]; y = j+dy[k]
            if in_range(x, y) and grid[x][y] == 1:
                cnt_1 += 1
        if cnt_1 >= 3:
            cnt += 1
print(cnt)