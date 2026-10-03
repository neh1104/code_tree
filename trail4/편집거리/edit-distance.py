A = input()
B = input()

# Please write your code here.
import sys
n, m = len(A), len(B)
INT_MAX = sys.maxsize

dp = [[INT_MAX]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = i
for j in range(m+1):
    dp[0][j] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] != B[j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        else:
            dp[i][j] = dp[i-1][j-1]

#print(*dp, sep = '\n')
print(dp[n][m])