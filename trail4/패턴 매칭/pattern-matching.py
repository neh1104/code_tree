s = input()
p = input()

# Please write your code here.
import sys
n, m = len(s), len(p)
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if p[j-1] == '*':
            last = p[j-2]
            if last == '.':
                print('true')
                sys.exit(0)
            else:
                I = i
                while I <= n and last == s[I-1]:
                    dp[I][j] = max(dp[i-1][j-1]+1, dp[I][j], dp[I-1][j]+1)
                    I+=1

        elif p[j-1] == '.':
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
        else:
            if s[i-1] == p[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1], dp[i][j])
        if dp[i][j] == n:
            print('true')
            sys.exit(0)
#print(*dp, sep = '\n')
print('false')