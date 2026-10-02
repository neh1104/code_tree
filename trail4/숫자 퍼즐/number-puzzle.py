n, m, K = map(int, input().split())

# Please write your code here.

dp = [[[0]*(m+1) for _ in range(m+1)] for _ in range(n+1)]
for k in range(1, m+1):
    dp[0][0][k] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(1, m+1):
            for w in range(k, j+1):
                dp[i][j][k] += dp[i-1][j-w][w]

curr = m
last = 1
result = []
for i in range(n, 0, -1):
    for j in range(last, curr+1):

        cnt = dp[i-1][curr-j][j]

        if K <= cnt:
            result.append(j)
            curr -= j
            last = j
            break
        else:
            K -= cnt

print(*result)