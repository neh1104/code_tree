n, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x = n//2; y = n//2
sum = board[x][y]
d = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def move():
    global d, x, y
    if i == 'L':
        d = (d+3)%4
        return 0
    elif i == 'R':
        d = (d+1)%4
        return 0
    else:
        if in_range(x+dr[d], y+dc[d]):
            x+=dr[d]; y+=dc[d]
            return board[x][y]
        else:
            return 0

def in_range(x, y):
    return 0<=x<n and 0<=y<n

for i in str:
    sum += move()

print(sum)

