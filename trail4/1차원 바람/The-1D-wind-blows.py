n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
wind = [input().split() for _ in range(q)]

def move_l(i):
    tmp = a[i][0]
    for j in range(m-1):
        a[i][j] = a[i][j+1]
    a[i][-1] = tmp

def move_r(i):
    tmp = a[i][-1]
    for j in range(m-1, 0, -1):
        a[i][j] = a[i][j-1]
    a[i][0] = tmp

def check(i, ud):
    ch = 0
    if i > 0 and ud == 'u':
        for j in range(m):
            if a[i][j] == a[i-1][j]:
                ch = 'u'
    if i < n-1 and ud == 'd':
        for j in range(m):
            if a[i][j] == a[i+1][j]:
                ch = 'd'
    return ch
    
def blow(i, d):
    if d == 'R':
        move_l(i)
    else:
        move_r(i)
    iu = i; id = i
    du = d; dd = d
    while check(iu, 'u') != 0:
        if du == 'R':
            move_r(iu-1)
            iu -= 1; du = 'L'
        else:
            move_l(iu-1)
            iu -= 1; du = 'R'
    while check(id, 'd') != 0:
        if dd == 'L':
            move_l(id + 1)
            id += 1; dd = 'R'
        else:
            move_r(id+1)
            id += 1; dd = 'L'

for i, d in wind:
    blow(int(i)-1, d)

for i in a:
    print(*i)