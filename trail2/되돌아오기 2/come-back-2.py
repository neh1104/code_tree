commands = input()

# Please write your code here.
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x,y = 0, 0
cnt = 0; d = 0
ch = True
for i in commands:
    if i == 'F':
        x += dx[d]
        y += dy[d]
    else:
        if i == 'L':
            d = (d+1)%4
        else:
            d = (d+3)%4
    cnt += 1
    if x == 0 and y == 0:
        print(cnt)
        ch = False
        break

if ch:
    print(-1)