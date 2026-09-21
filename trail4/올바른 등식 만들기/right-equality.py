N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

dp = [0 for _ in range(41)]
dp[20] = 1

for num in nums:
    ndp = [0 for _ in range(41)]
    for j in range(41):
        if dp[j] == 0:
            continue
        
        if j+num < 41:
            ndp[j+num] += dp[j]
        if j-num >= 0:
            ndp[j-num] += dp[j]
    dp = ndp

print(dp[20+M])