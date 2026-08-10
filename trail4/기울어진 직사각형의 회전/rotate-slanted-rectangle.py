n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
q = list(map(int, input().split()))

r, c, m1, m2, m3, m4, dir = q
r -= 1; c -= 1

A = a[r-m1][c+m1]; B = a[r-m1-m2][c+m1-m2]; C = a[r-m2][c-m2]

def turn(r, c, dir):
    if dir == 0:
        dr = [-1, -1, 1, 1]
        dc = [1, -1, -1, 1]
        M = [m1, m2, m3, m4]
        spot = [0, A, B, C]
    else:
        dr = [-1, -1, 1, 1]
        dc = [-1, 1, 1, -1]
        M = [m4, m3, m2, m1]
        spot = [0, C, B, A]
    for i in range(4):
        m = M[i]
        for l in range(m, 0, -1):
            a[r+l*dr[i]][c+l*dc[i]] = a[r+(l-1)*dr[i]][c+(l-1)*dc[i]]
        r += m*dr[i]; c += m*dc[i]
        if i != 0:
            I = (i+2)%4
            a[r+m*dr[I]+dr[i]][c+m*dc[I]+dc[i]] = spot[i]
            #print(spot[i])
turn(r, c, dir)

for i in a:
    print(*i)