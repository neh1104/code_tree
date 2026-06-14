n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

ls = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def c_m(x, y):
    return 0<=x<n and 0<=y<m and ls[x][y] == 0 

dr = [0, 1, 0, -1]; dc = [1, 0, -1, 0]
cnt = 1
x = 0; y = 0
d = 0
for _ in range(n*m):
    ls[x][y] = cnt
    if not(c_m(x+dr[d], y+dc[d])):
        d = (d+1)%4
    x += dr[d]
    y += dc[d]
    cnt += 1

for i in ls:
    print(*i)