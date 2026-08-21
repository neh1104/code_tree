n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    for j in range(n):
        a[i][j] = [a[i][j]]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def find_xy(x, y):
    FMAX = 0
    Mr = x; Mc = y
    for d in range(8):
        i = x+dr[d]; j = y+dc[d]
        if in_range(i, j):
            if a[i][j] != []:
                MAX = max(a[i][j][:])
            else:
                MAX = 0
            if MAX > FMAX:
                Mr = i; Mc = j
                FMAX = MAX
    return Mr, Mc

def move(x, y, mr, mc, idx):
    global a
    #print(a[x][y][idx:])
    for n in a[x][y][idx:]:
        a[mr][mc].append(n)
    del a[x][y][idx:]

for k in move_nums:
    for i in range(n):
        for j in range(n):
            if k in a[i][j]:
                idx = a[i][j].index(k)
                mr, mc = find_xy(i, j)
                if (i, j) != (mr, mc):
                    move(i, j, mr, mc, idx)
                break
        else:
            continue
        break

for i in range(n):
    for j in range(n):
        if a[i][j] == []:
            print('None')
        else:
            print(*reversed(a[i][j]))