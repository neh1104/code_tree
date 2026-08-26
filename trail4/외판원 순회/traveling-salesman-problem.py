n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
vt = [-1 for i in range(n)]
ls = []; MIN = sys.maxsize

def cycle(vt):
    x = 0; cnt = 0
    while x != -1:
        x = vt[x]
        cnt += 1
        if cnt == n:
            break
        if x == 0:
            return True
    return False

def choose(curr, d):
    global vt
    global ls
    global MIN
    
    if d >= MIN:
        return

    if cycle(vt):
        return

    if curr == n:
        #print(ls, sum(ls), vt)
        MIN = min(MIN, sum(ls))
        return
    

    for i in range(n):
        if A[curr][i] == 0 or vt[i] != -1:
            continue

        vt[i] = curr; ls.append(A[curr][i])
        choose(curr+1, d+A[curr][i])
        vt[i] = -1; ls.pop()

choose(0, 0)
print(MIN)