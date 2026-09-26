n, k = map(int, input().split())
str = input()

# Please write your code here.
INT_MIN = -1000000
dp = [[[INT_MIN]*2 for _ in range(k+2)] for _ in range(n+1)]
dp[0][1][0] = 0

for i in range(1, n+1):
    for j in range(1, k+2):
        dp[i][j][0] = max(dp[i-1][j-1][1], dp[i-1][j][0])+(str[i-1]=='L')
        dp[i][j][1] = max(dp[i-1][j-1][0], dp[i-1][j][1])+(str[i-1]=='R')

#print(*dp, sep = '\n')
print(max(max(arr) for arr in dp[n]))