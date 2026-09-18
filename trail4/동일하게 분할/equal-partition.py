n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

s = sum(arr)
if s%2 == 0:
    dp = [0]*(2*s+1)
    dp[s] = 1
    for x in arr:
        ndp = [0]*(2*s+1)
        for i in range(2*s+1):
            if dp[i]:
                if i+x < 2*s+1:
                    ndp[i+x] = 1
                if i-x >= 0:
                    ndp[i-x] = 1
        dp = ndp

    print('Yes' if dp[s] else 'No')

else:
    print('No')