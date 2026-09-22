N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys
INT_MIN = -sys.maxsize

dp = [[[INT_MIN]*2 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0][0] = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0])+numbers[i-1]

        dp[i][j][0] = max(dp[i-1][j])

#print(*dp, sep = '\n')
print(max(dp[N][M]))