n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

dp = [-1 for _ in range(m+1)]
dp[0] = 0
for i in range(m):
    if dp[i] == -1:
        continue

    for j in range(n):

        if dp[i] >= j:
            continue
        idx = i+A[j]
        if idx > m:
            continue
        if dp[idx] != -1 and dp[idx] <= j:
            continue

        dp[idx] = j

print('Yes' if dp[m] != -1 else 'No')