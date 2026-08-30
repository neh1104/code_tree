n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
import sys
iMAX = sys.maxsize

vt = [iMAX for _ in range(m+1)]
vt[0] = 0

for a in A:
    for c in range(m, a-1, -1):
        if vt[c-a] == iMAX:
            continue
        vt[c] = min(vt[c], vt[c-a]+1)


if vt[m] == iMAX:
    print(-1)
else:
    print(vt[m])