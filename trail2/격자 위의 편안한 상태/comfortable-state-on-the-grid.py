n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

ls = [
    [0 for _ in range(n)]
    for _ in range(n)
]

x, y = 0, 0
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
def in_range(x, y):
    return 0<= x< n and 0<=y<n

for r, c in points:
    ls[r-1][c-1] = 1
    cnt = 0
    for i in range(4):
        if in_range(r-1+dx[i], c-1+dy[i]):
            if ls[r+dx[i]-1][c+dy[i]-1] == 1:
                cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)