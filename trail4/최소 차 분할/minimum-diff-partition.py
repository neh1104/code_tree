n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
T = sum(arr)
t = T//2

dp = [-1]*(t+1)
dp[0] = 0

for i in range(n):
    for j in range(t, arr[i]-1, -1):
        dp[j] = max(dp[j], dp[j-arr[i]]+arr[i])

MAX = max(dp)

print(T-2*MAX)