n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
vt = [0 for i in range(n)]
MIN = sys.maxsize

def choose(curr, d, cnt):
    global MIN

    if d >= MIN:
        return

    if cnt == n:
        if A[curr][0] == 0:
            return
        MIN = min(MIN, d+A[curr][0])
        return

    for i in range(n):
        if A[curr][i] == 0 or vt[i] == 1:
            continue

        vt[i] = 1
        choose(i, d+A[curr][i], cnt+1)
        vt[i] = 0

vt[0] = 1
choose(0, 0, 1)
print(MIN)