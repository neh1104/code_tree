n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
import sys
cnt = 0
idx = [() for _ in range(11)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == '.':
            continue

        if grid[i][j] == 'S':
            idx[9] = (i, j)
        elif grid[i][j] == 'E':
            idx[10] = (i, j)
        else:
            cnt += 1
            idx[int(grid[i][j])-1] = (i, j)

tmp = []
for i in idx:
    if i != ():
        #print(i)
        tmp.append(i)

idx = tmp
def move(ls):
    length = 0
    last = idx[-2]

    for i in ls:
        length += abs(last[0] - i[0]) + abs(last[1] - i[1])
        last = i

    length += abs(last[0] - idx[-1][0]) + abs(last[1] - idx[-1][1])

    return length

ls = []; MIN = sys.maxsize
#print(idx)
def choose(curr, d):
    global ls
    global MIN

    if d == 3:
        p = move(ls)
        if p < MIN:
            #print(ls)
            MIN = p
        return

    if curr == cnt:
        return


    ls.append(idx[curr])
    choose(curr+1, d+1)
    ls.pop()
    #print('pop')

    choose(curr+1, d)

if cnt < 3:
    print(-1)
else:    
    choose(0, 0)
    print(MIN)