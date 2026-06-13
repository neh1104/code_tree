dirs = input()

# Please write your code here.
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
state = 400003; nof = 1
xy = [0,0]
for i in dirs:
    if i == 'F':
        xy = [xy[0]+dx[state%4], xy[1]+dy[state%4]]
        nof = 0
    if i == 'L':
        state -= 1
    if i == 'R':
        state += 1

if nof:
    print(0, 0)
else:
    print(*xy)