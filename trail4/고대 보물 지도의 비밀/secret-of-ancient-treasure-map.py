n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(1, n + 1):
    if numbers[i] < 0: continue
    dp[0][i] = max(numbers[i], dp[0][i - 1] + numbers[i])

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - (numbers[j] < 0)][j - 1] + numbers[j], numbers[j])

# print(*dp, sep='\n')
print(max(dp[k][1:]))

