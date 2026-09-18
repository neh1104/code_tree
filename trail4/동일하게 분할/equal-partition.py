n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

s = sum(arr)
if s%2 == 0:
    dp = [-1]*(2*s+1)
    dp[s] = 0
    for x in arr:
        ndp = [-1]*(2*s+1)
        for i in range(2*s+1):
            if dp[i] == -1:
                continue

            if i+x < 2*s+1:
                ndp[i+x] = max(ndp[i+x], dp[i]+x)
            if i-x >= 0:
                ndp[i-x] = max(ndp[i-x], dp[i]+x)
        dp = ndp
    #print(dp[s], dp)
    print('Yes' if dp[s] != -1 else 'No')

else:
    print('No')