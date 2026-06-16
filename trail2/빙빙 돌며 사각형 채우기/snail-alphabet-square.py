n, m = map(int, input().split())

# Please write your code here.

c = ord('A')

ls = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x<n and 0<=y<m and ls[x][y] == 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
x, y = 0, 0
for _ in range(n*m):
    ls[x][y] = chr(c)
    c += 1
    if c > ord('Z'):
        c = ord('A')
    if not(in_range(x+dr[d], y+dc[d])):
        d = (d+1)%4
    x += dr[d]
    y += dc[d]

for i in ls:
    print(*i)