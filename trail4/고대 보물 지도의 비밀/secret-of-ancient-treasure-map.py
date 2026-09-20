n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.

import sys

INT_MIN = -sys.maxsize
dp = [[INT_MIN for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    x = numbers[i - 1]

    if x < 0:
        if k >= 1:
            dp[i][1] = x

        for j in range(1, k + 1):
            if dp[i - 1][j - 1] != INT_MIN:
                dp[i][j] = dp[i - 1][j - 1] + x

    else:
        dp[i][0] = x

        for j in range(k + 1):
            if dp[i - 1][j] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + x)

answer = INT_MIN

for i in range(1, n + 1):
    answer = max(answer, max(dp[i]))

print(answer)