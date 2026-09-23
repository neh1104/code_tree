n = int(input())

# Please write your code here.
mod = 10**9+7

dp = [[0]*10 for _ in range(n)]
for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%mod

#print(*dp, sep = '\n')
print(sum(dp[n-1])%mod)