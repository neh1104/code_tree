n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
vt = [0 for i in range(n)]
MIN = sys.maxsize
c = [0 for _ in range(n)]
def choose(curr, d, cnt):
    global vt
    global MIN
    global c

    if d >= MIN:
        return

    if cnt == n:
        #print(ls, d, vt)
        #print(ls)
        MIN = min(MIN, d+A[curr][0])
        return
    if c[curr] == 1:
        return
    c[curr] = 1

    for i in range(n):
        if A[curr][i] == 0 or vt[i] != 0:
            continue

        vt[i] = 1
        #print(curr, i)
        #print(ls)
        choose(i, d+A[curr][i], cnt+1)
        vt[i] = 0
    c[curr] = 0

choose(0, 0, 0)
print(MIN)