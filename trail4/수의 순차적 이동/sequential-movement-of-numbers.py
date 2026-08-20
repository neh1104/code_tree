n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0<=x<n and 0<=y<n

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, 1, -1, -1, 1, 0]

def move(i, j):
    MAX = 0
    for d in range(8):
        if in_range(i+dr[d], j+dc[d]) and a[i+dr[d]][j+dc[d]] > MAX:
            MAX = a[i+dr[d]][j+dc[d]]
            MAX_R = i+dr[d]; MAX_C = j+dc[d]
    return MAX_R, MAX_C

for _ in range(m):
    for key in range(1, n*n+1):
        #격자 탐색
        for i in range(n):
            for j in range(n):
                if a[i][j] == key:
                    x, y = move(i, j)
                    a[i][j], a[x][y] = a[x][y], a[i][j]
                    #for i in a:
                    #    print(*i)
                    #print()
                    break
            else:
                continue
            break

for i in a:
    print(*i)
