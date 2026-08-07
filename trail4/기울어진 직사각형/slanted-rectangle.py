n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def rectangle(i, j):
    x, y = i, j
    #print(i, j, 'i,j')
    MAX = 0
    for d1 in range(1, min(i, n-j-1)+1):
        for d2 in range(1, min(i-d1, j)+1):
            sum = 0
            for m1 in range(d1):
                x += dr[0]; y += dc[0]
                sum += a[x][y]
            #print(x, y, 'f')
            for m2 in range(d2):
                x += dr[1]; y += dc[1]
                if in_range(x, y):
                    sum += a[x][y] 
                #else:
                 #   sum -= 20000       
            #print(x, y, 's')
            for m3 in range(d1):
                x += dr[2]; y += dc[2]
                if in_range(x, y):
                    sum += a[x][y]
                #else:
                 #   sum -= 20000
            #print(x, y, 't')
            for m4 in range(d2):
                x += dr[3]; y += dc[3]
                if in_range(x, y):
                    sum += a[x][y]
                #else:
                 #   sum -= 20000
            #print(x, y, 'f')
            #print(sum)
            MAX = max(MAX, sum)
    return MAX

MAX = 0
for i in range(2, n):
    for j in range(1, n-1):
        result = rectangle(i, j)
        MAX = max(MAX, result)

print(MAX)