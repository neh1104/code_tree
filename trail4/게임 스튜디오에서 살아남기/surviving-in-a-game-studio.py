n = int(input())

# Please write your code here.

dp = [[[0 for _ in range(3)] for _ in range(n+1)] for _ in range(4)]
dp[0][0][0] = 1
for t in range(3):
    for i in range(1, n+1):
        s = sum(dp[t][i-1][:])
        dp[t][i][0] += s
        dp[t+1][i][0] += s 
        for j in range(1, 3):
            dp[t][i][j] = dp[t][i-1][j-1]

SUM = sum(sum(arr[n]) for arr in dp[:3])
print(SUM%(10**9+7))