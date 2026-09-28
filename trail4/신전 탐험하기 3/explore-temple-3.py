N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

dp = [[0 for _ in range(M)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(M):
        A = a[i-1][j]
        for k in range(M):
            if k != j:
                dp[i][j] = max(dp[i][j], dp[i-1][k]+A)
#print(*dp, sep = '\n')
print(max(dp[N]))