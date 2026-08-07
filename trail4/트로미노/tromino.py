n, m = map(int, input().split())

a = [
    list(map(int, input().split())) for _ in range(n)
]
#print(a)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [1, 1, -1, -1, 0]
dy = [1, 0, 1, 0, 2]
MAX = 0
for i in range(n):
    for j in range(m):
        if in_range(i, j+1):
            duo = a[i][j] + a[i][j+1]
            #print(a[i][j])
            for d in range(5):
                if in_range(i+dx[d], j+dy[d]):
                    sum = 0
                    sum += duo + a[i+dx[d]][j+dy[d]]
             #       print(a[i+dx[d]][j+dy[d]], end = ' ')
                MAX = max(sum, MAX)
        if i <= n-3:
        #   print(a[i+2][j], end= ' ')
            MAX = max(a[i][j]+a[i+1][j]+a[i+2][j], MAX)
        #print()

print(MAX)