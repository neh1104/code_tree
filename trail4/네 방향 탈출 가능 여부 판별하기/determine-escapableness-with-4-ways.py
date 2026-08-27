n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

vt = [[0 for _ in range(m)] for _ in range(n)]
q = [(0, 0)]
r = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<m and vt[x][y] == 0 and a[x][y] != 0

def bfs():
    while q:
        r, c = q.pop(0)
        if r == n-1 and c == m-1:
            print(1)
            return

        for d in range(4):
            x = r + dr[d]; y = c + dc[d]
            if in_range(x, y):
                q.append((x, y))
                vt[x][y] = 1
    print(0)

bfs()
