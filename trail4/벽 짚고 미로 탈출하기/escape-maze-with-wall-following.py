n = int(input())
x, y = map(int, input().split())
a = [input() for _ in range(n)]
x-=1; y-=1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def wall(x, y, d):
    #오른쪽 짚을 벽이 있는 경우
    if a[x+dr[(d+1)%4]][y+dc[(d+1)%4]] == '#':
        #앞이 막힌경우
        if in_range(x+dr[d], y+dc[d]) and a[x+dr[d]][y+dc[d]] == '#':
            return (d+3)%4
        #앞이 막히지 않은 경우
        else:
            return d
    #짚을 벽이 없는 경우
    return (d+1)%4

vst = [[[0] * 4 for _ in range(n)] for _ in range(n)]
cnt = 0; d = 0
while True:

    d = wall(x, y, d)
    x_n = x+dr[d]; y_n = y+dc[d]

    if not(in_range(x_n, y_n)):
        cnt+=1
        break

    if a[x_n][y_n] != '#':
        x = x_n; y = y_n
        cnt += 1

    if vst[x][y][d] == 1:
        cnt = -1
        break
    vst[x][y][d] = 1
    
        
print(cnt)