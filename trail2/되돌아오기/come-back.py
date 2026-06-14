N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dr = {'W': 0, 'S': 1, 'N': -1, 'E': 0}
dc = {'W': -1, 'S': 0, 'N': 0, 'E': 1}
x, y = 0, 0
cnt = 0; ch = False

for d, l in zip(dir, dist):
    for i in range(1, l+1):
        x = x+dr[d]*1
        y = y+dc[d]*1
        cnt += 1
        #print(x, y)
        if x == 0 and y == 0:
            print(cnt)
            ch = True
    if ch:
        break
if not(ch):
    print(-1)