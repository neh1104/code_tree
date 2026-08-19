n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.

def in_range(x, y):
    return 0<=x<n and 0<=y<n

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(i, j):
    MAX = 0
    for d in range(4):
        if in_range(i+dr[d], j+dc[d]):
            if a[i+dr[d]][j+dc[d]] > MAX:
                MAX = a[i+dr[d]][j+dc[d]]
                MAX_R = i+dr[d]; MAX_C = j+dc[d]
    return MAX_R, MAX_C

tmp = [[0 for _ in range(n)] for _ in range(n)]
for x, y in zip(r, c):
    tmp[x-1][y-1] = 1

for _ in range(t):
    ttmp = [[0 for _ in range(n)] for _ in range(n)]
    ls = []
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 1:
                R, C = move(i, j)
                ttmp[R][C] += 1
                ls.append((R, C))

    #충돌한 구슬 없애기
    for R, C in ls:
        if ttmp[R][C] >= 2:
            ttmp[R][C] = 0

    tmp = ttmp
    #print(*tmp, sep = '\n')
    #print()

cnt = 0
for i in tmp:
    cnt += i.count(1)

print(cnt)