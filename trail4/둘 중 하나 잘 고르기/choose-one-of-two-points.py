n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.
int_min = -1000000
dp = [[int_min for _ in range(n+1)] for _ in range(2*n+1)]
dp[0][0] = 0
for j in range(1, 2*n+1):
    dp[j][0] = dp[j-1][0]+blue[j-1]

for i in range(1, 2*n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j]+blue[i-1], dp[i-1][j-1]+red[i-1])

#print(*dp, sep = '\n')
print(dp[2*n][n])