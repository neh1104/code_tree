n = int(input())
coin = [0]+list(map(int, input().split()))

# Please write your code here.
import sys
INT_MIN = -sys.maxsize
vt = [[INT_MIN for _ in range(4)] for _ in range(n+1)]
vt[0][0] = 0
vt[1][1] = coin[1]

for i in range(2, n+1):
    vt[i][0] = vt[i-2][0]+coin[i]
    for j in range(1, 4):
        vt[i][j] = max(vt[i-1][j-1], vt[i-2][j]) + coin[i]

print(max(vt[n]))