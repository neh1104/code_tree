b = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
#print(*board, sep = '\n')
n = 19
def in_range(x, y):
    return not(0<=x<n and 0<=y<n)

M = []
def rkfh(x, y):
    global M
    for i in range(1, 5):
        if in_range(x, y+i) or b[x][y+i] != N:
            return 0
    M.append(x+1)
    M.append(y+3)
    return 1

def tpfh(x, y):
    global M
    for i in range(1, 5):
        if in_range(x+i, y) or b[x+i][y] != N:
            return 0
    M.append(x+3)
    M.append(y+1)
    return 1

def eorkr1(x, y):
    global M
    for i in range(1, 5):
        if in_range(x+i, y+i) or b[x+i][y+i] != N:
            return 0
    M.append(x+3)
    M.append(y+3)
    return 1

def eorkr2(x, y):
    global M
    for i in range(1, 5):
        if in_range(x+i, y-i) or b[x+i][y-i] != N:
            return 0
    M.append(x+3)
    M.append(y-1)
    return 1
ch = True
for i in range(n):
    for j in range(n):
        N = b[i][j]
        if N == 1 or N == 2:
            if rkfh(i,j) or tpfh(i,j) or eorkr1(i,j) or eorkr2(i,j):
                print(N)
                print(*M)
                ch = False
                break
if ch:
    print(0)
