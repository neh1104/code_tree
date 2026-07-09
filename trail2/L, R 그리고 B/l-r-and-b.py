board = [list(input()) for _ in range(10)]

# Please write your code here.

for i, bd in enumerate(board):
    for b in range(len(bd)):
        if bd[b] == 'L':
            Lx, Ly = (i, b)
        if bd[b] == 'B':
            Bx, By = (i, b)
        if bd[b] == 'R':
            Rx, Ry = (i, b)
x = abs(Lx-Bx)
y = abs(Ly-By)

if ((Lx == Bx and Lx == Rx) or (Ly == By and Ly == Ry)) and (Lx-Rx)*(Bx-Rx) + (Ly-Ry)*(By-Ry) < 0:
    print(x+y+1)
else:
    print(x+y-1)