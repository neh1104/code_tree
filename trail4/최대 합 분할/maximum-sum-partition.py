n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
S = sum(arr)
dp = [-1]*(2*S+1)
dp[S] = 0

for i in range(n):
    new_dp = dp[:]
    for j in range(2*S+1):
        if dp[j] == -1:
            continue

        if arr[i]+j < 2*S+1:
            new_dp[arr[i]+j] = max(new_dp[arr[i]+j], dp[j]+arr[i])
            #print(i, j, '+')

        if j-arr[i] >= 0:
            new_dp[j-arr[i]] = max(new_dp[j-arr[i]], dp[j]+arr[i])
            #print(i, j, '-')
    dp = new_dp

print(dp[S]//2)