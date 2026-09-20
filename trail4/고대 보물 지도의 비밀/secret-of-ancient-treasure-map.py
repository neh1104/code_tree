n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.

dp = [[-10001]*(k+1) for _ in range(n)]
if numbers[0] < 0:
    dp[0][1] = numbers[0]
else:
    dp[0][0] = numbers[0]

for i in range(1, n):
    if numbers[i] < 0:
        for count in range(1, k+1):
            if dp[i-1][count-1] == -10001:
                continue
            dp[i][count] = max(dp[i-1][count-1], 0) + numbers[i]
    else:
        for count in range(k+1):
            dp[i][count] = max(0, dp[i-1][count]) + numbers[i]
print(max([max(row) for row in dp]))
