n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    v.append(int(vi))

# Please write your code here.
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
dt = {'U':0, 'L':1, 'D':2, 'R':3}

a = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    a[r[i]-1][c[i]-1].append((dt[d[i]], v[i], i))

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def move(i, j, d, v):
    x = i; y = j
    for _ in range(v):
        x += dr[d]; y += dc[d]
        if not(in_range(x, y)):
            d = (d+2)%4
            x += dr[d]*2; y += dc[d]*2
    return x, y, d

for _ in range(t):
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    gs = [[0 for _ in range(n)] for _ in range(n)]
    ls = []
    for i in range(n):
        for j in range(n):
            if len(a[i][j]) != 0:
                for ad, av, gn in a[i][j]:
                    x, y, d = move(i, j, ad, av)
                    tmp[x][y].append((d, av, gn))
                    gs[x][y] += 1
                    if not((x,y) in ls):
                        ls.append((x, y))
    #print(*tmp, sep = '\n')
    for i, j in ls:
        if gs[i][j] > k:
            tmp[i][j].sort(key=lambda x: (-x[1], -x[2]))
            for _ in range(gs[i][j]-k):
                tmp[i][j].pop()
    
    a = tmp


cnt = 0
for i in range(n):
    for j in range(n):
        #print(a[i][j])
        cnt += len(a[i][j])

print(cnt)