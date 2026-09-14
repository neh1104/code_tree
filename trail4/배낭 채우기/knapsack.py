N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

dp = [0] * (M + 1)

for i in range(N):
    for j in range(M, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(max(dp))