N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))

# Please write your code here.

dp = [[[0]*4 for _ in range(M+2)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+2):
        for k in range(4):
            l = dp[i-1][j-1]
            dp[i][j][k] = max(l[(k+1)%4], l[(k+2)%4], l[(k+3)%4], dp[i-1][j][k])
            if a[i] == k+1:
                dp[i][j][k]+=1

#print(*dp, sep = '\n')
print(max(dp[N][M+1]))