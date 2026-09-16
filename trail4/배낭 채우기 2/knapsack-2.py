N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

dp = [-1]*(M+1)
dp[0] = 0

for i in range(M):
    if dp[i] == -1:
        continue
    for j in range(N):
        if i+w[j] > M:
            continue
        dp[i+w[j]] = max(dp[i+w[j]], dp[i]+v[j])

print(max(dp))