n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r-=1; c-=1
# Please write your code here.

def in_range(x, y):
    return 0<=x<n and 0<=y<n

bk = a[r][c]-1

tmp = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == r and abs(j-c) <= bk:
            a[i][j] = 0
        elif j == c and abs(i-r) <= bk:
            a[i][j] = 0

for j in range(n):
    tmp = []
    for i in range(n):
        if a[i][j] != 0:
            tmp.append(a[i][j])
    tmp.reverse()
    for _ in range(n-len(tmp)):
        tmp.append(0)
    
    for i in range(n):
       a[n-i-1][j] = tmp[i]

    
for i in a:
    print(*i)