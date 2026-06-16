n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

x, y = n-1, n-1
cnt = n*n
ls = [
    [0 for _ in range(n)]
    for _ in range(n)
]   

def in_range(x, y):
    return 0<=x<n and 0<=y<n and ls[x][y] == 0

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
d = 0
for _ in range(n*n):
    ls[x][y] = cnt
    cnt -= 1
    if not(in_range(x+dr[d], y+dc[d])):
        d = (d+1)%4
    x += dr[d]
    y += dc[d]
    
for i in ls:
    print(*i)