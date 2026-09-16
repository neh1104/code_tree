n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.

dp = [-1]*(n+1)
dp[0] = 0
for i in range(n):
    if dp[i] == -1:
        continue
    for j in range(n):
        if i+j+1 > n:
            continue
        dp[i+j+1] = max(dp[i+j+1], dp[i]+profit[j])
print(dp[n])