n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

rdir = [0, -1, 1, 0]
cdir = [-1, 0, 0, 1]
r-= 1; c-= 1
def in_range(x, y):
    return 0<=x<n and 0<=y<n
if d == 'R':
    dir = 3
elif d == 'D':
    dir = 2
elif d == 'U':
    dir = 1
else:
    dir = 0

for i in range(t):
    if in_range(r+rdir[dir], c+cdir[dir]):
        r += rdir[dir]; c += cdir[dir]
    else:
        dir = 3 - dir

print(r+1, c+1)