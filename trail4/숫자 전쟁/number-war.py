n = int(input())
f = list(map(int, input().split()))
s = list(map(int, input().split()))

# Please write your code here.

dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0] = s[0]*(s[0]<f[0])
f.append(0); s.append(0)

for i in range(n):
    for j in range(n):
        if dp[i][j] != -1:
            F = f[j]; S = s[i]

            dp[i+1][j+1] = max(0, dp[i][j])+s[i+1]*(s[i+1] < f[j+1])

            if S < F: #이기는 경우  
                dp[i+1][j] = max(dp[i+1][j], dp[i][j]+s[i+1]*(s[i+1] < f[j]))
            
            elif S > F:
                dp[i][j+1] = max(dp[i][j+1], dp[i][j]+s[i]*(s[i] < f[j+1]))

            
MAX = 0
for i in range(n):
    MAX = max(MAX, dp[n-1][i])

print(MAX)