n, m = map(int, input().split())

# Please write your code here.

ls = [
    [0 for _ in range(m)]
    for _ in range(n)
]

x, y = 0, 0
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
d = 0
def cm(x, y):
    return 0<=x<n and 0<=y<m and ls[x][y] == 0
cnt = 1
for _ in range(n*m):
    ls[x][y] = cnt
    cnt +=1
    if not(cm(x+dr[d], y+dc[d])):
        d = (d+1)%4 
    x += dr[d]
    y += dc[d]

for i in ls:
    print(*i)