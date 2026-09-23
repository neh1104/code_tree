n = int(input())
s = []
b = []
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

# Please write your code here.
import sys
INT_MIN = -sys.maxsize

dp = [[[INT_MIN]*11 for _ in range(13)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 0

for i in range(1, n+1):
    for j in range(12):
        for k in range(10):
            S = -1 if dp[i-1][j-1][k] == INT_MIN else s[i-1]
            B = -1 if dp[i-1][j][k-1] == INT_MIN else b[i-1]
            dp[i][j][k] = max(dp[i-1][j-1][k]+S, dp[i-1][j][k-1]+B, dp[i-1][j][k])

print(dp[n][11][9])
#print(*dp, sep = '\n')