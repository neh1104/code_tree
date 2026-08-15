n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def couple(tmp):
    cnt = 0
    for i in range(n):
        for j in range(n):
            key = tmp[i][j]
            for d in range(2):
                if in_range(i+dr[d], j+dc[d]) and key == tmp[i+dr[d]][j+dc[d]] and key != 0:
                    cnt += 1
    return cnt

def bomb(i, j):
    l = a[i][j]
    tmp = [row[:] for row in a]
    tmp[i][j] = 0
    for k in range(1, l):
        for d in range(4):
            x = i+dr[d]*k
            y = j+dc[d]*k
            if in_range(x, y):
                tmp[x][y] = 0
    
    ##down
    for y in range(n):
        n_idx = 0
        ttmp = [0 for _ in range(n)]
        for x in range(n):
            if tmp[n-1-x][y]:
                #print(tmp[n-1-x][y], end='')
                ttmp[n_idx] = tmp[n-1-x][y]
                n_idx += 1
        #print(ttmp)
        for x in range(n):
            tmp[n-1-x][y] = ttmp[x]
    #for i in tmp:
    #    print(*i)
    #print(couple(tmp))
    return couple(tmp)

MAX = 0
for i in range(n):
    for j in range(n):
        MAX = max(MAX, bomb(i, j))

print(MAX)