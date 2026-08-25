n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

r-=1; c-=1
MAX = 0
def wornl(r, c, moved):
    global MAX
    #print(r, c)
    d = move_dir[r][c]
    for l in range(1, n):
        if not(in_range(r+dr[d]*l, c+dc[d]*l)):
            MAX = max(MAX, moved)
            #print(r, c, l, 'over')
            return
        if num[r+dr[d]*l][c+dc[d]*l] < num[r][c]:
            MAX = max(MAX, moved)
            #print(r, c, l, 'smaller')
            continue
        wornl(r+dr[d]*l, c+dc[d]*l, moved+1)

wornl(r, c, 0)
print(MAX)