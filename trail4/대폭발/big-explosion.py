n, m, r, c = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(n)]
a[r-1][c-1] = 1

def in_range(x, y):
    return 0<=x<n and 0<=y<n

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bomb(i, j, t):
    global tmp
    for d in range(4):
        x = i + 2**(t-1)*dr[d]; y = j + 2**(t-1)*dc[d]
        if in_range(x, y):
            tmp[x][y] = 1

for t in range(1, m+1):
    tmp = [i[:] for i in a]
    #print(*tmp, sep = '\n')
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                bomb(i, j, t)
    #print()
    a = tmp

s = 0
for i in a:
    s += sum(i)
    #print(*i)
print(s)