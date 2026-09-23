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

dp = [[[INT_MIN]*10 for _ in range(12)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 0

for i in range(1, n+1):
    for j in range(12):
        for k in range(10):
            dp[i][j][k] = dp[i-1][j][k]

            # 축구팀에 넣는 경우
            if j > 0 and dp[i-1][j-1][k] != INT_MIN:
                dp[i][j][k] = max(
                    dp[i][j][k],
                    dp[i-1][j-1][k] + s[i-1]
                )

            # 야구팀에 넣는 경우
            if k > 0 and dp[i-1][j][k-1] != INT_MIN:
                dp[i][j][k] = max(
                    dp[i][j][k],
                    dp[i-1][j][k-1] + b[i-1]
                )

print(dp[n][11][9])
#print(*dp, sep = '\n')