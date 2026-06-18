n, m = map(int, input().split())
arr = [input() for _ in range(n)]

# Please write your code here.
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
cnt = 0
def in_range(x, y):
    return 0<=x<n and 0<=y<m
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            for d in range(8):
                if in_range(i+dx[d]*2, j+dy[d]*2):
                    if arr[i+dx[d]][j+dy[d]] == 'E' and arr[i+dx[d]*2][j+dy[d]*2] == 'E':
                        cnt += 1
print(cnt)