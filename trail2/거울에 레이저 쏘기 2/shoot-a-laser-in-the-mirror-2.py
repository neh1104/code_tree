n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
def in_range(x, y):
    return 0<=x<n and 0<=y<n

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

def reflect(d, c):
    if c == '/':
        if d %2 == 0:
            d = (d+1)%4
        else:
            d = (d+3)%4
    if c == '\\':
        #print('I got')
        if d % 2== 0:
            d = (d+3)%4
        else:
            d = (d+1)%4
    return d
k -= 1
d = k // n
#how to choice the start point??
if d == 0:
    x = 0
    y = k
elif d == 1:
    y = n-1
    x = k % n
elif d == 2:
    x = n-1
    y = n-(k%n)-1
else:
    y = 0
    x = n-(k%n)-1

cnt = 0
while True:
    if not(in_range(x, y)):
        print(cnt)
        break
    C = grid[x][y]
    #print(C)
    d = reflect(d, C)
    cnt += 1
    x = x+dr[d]
    y = y+dc[d]
    #print(x, y)