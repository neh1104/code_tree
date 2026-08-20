T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
df = {'U':0, 'D':2, 'R':1, 'L':3}
def in_range(x, y):
        return 0<=x<n and 0<=y<n
def move(i, j, d):
    x = i+dr[d]; y = j+dc[d]
    if in_range(x, y):
        return x, y, d
    d = (d+2)%4
    return i, j, d

for _ in range(T):
    n, M = map(int, input().split())
    x, y, d = [], [], []
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        d.append(di)

    # Please write your code here.
    a = [[-1 for _ in range(n)] for _ in range(n)]
    ls = []
    for i in range(M):
        a[x[i]-1][y[i]-1] = df[d[i]]
        #ls.insert(0, (x[i]-1, y[i]-1, df[d[i]]))
    #print(*a, sep = '\n')
    
    for _ in range(2*n):
        tmp = [[0 for _ in range(n)] for _ in range(n)]
        ttmp = [[-1 for _ in range(n)] for _ in range(n)]
        ls = []
        for i in range(n):
            for j in range(n):
                if a[i][j] != -1:
                    r, c, d = move(i, j, a[i][j])
                    tmp[r][c] += 1
                    ttmp[r][c] = d
                    ls.append((r, c))
        #print(*a, sep='\n')
        for i, j in ls:
            #print(i, j)
            if tmp[i][j] != 1:
                ttmp[i][j] = -1
        a = ttmp

    cnt = 0
    for i in a:
    #   print(*i)
        cnt += i.count(-1)
    print(n*n-cnt)
    #print()