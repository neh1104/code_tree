N = int(input())
a = input()
b = input()

# Please write your code here.
import sys
INT_MAX = sys.maxsize

dp = [[INT_MAX for _ in range(10)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(10):
        now = (int(a[i])+j)%10
        toque = (int(b[i]) - now+10)%10
        
        if dp[i][j] != INT_MAX:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+10-toque)
            dp[i+1][(j+toque)%10] = min(dp[i+1][(j+toque)%10], dp[i][j]+toque)
            #print(a[i], now, (now+toque)%10, toque)
            #print(now, (now+toque)%10, toque)
#print(*dp, sep= '\n')

print(min(dp[N]))