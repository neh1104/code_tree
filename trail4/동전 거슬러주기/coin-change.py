N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
import sys
MAX = sys.maxsize

vt = [MAX for _ in range(M+1)]
vt[0] = 0
for i in range(M+1):
    for j in coin:
        if j>i:
            continue
        if vt[i-j] == MAX:
            continue
        vt[i] = min(vt[i], vt[i-j]+1)
if vt[M] == MAX:
    print(-1)
else:
    print(vt[M])