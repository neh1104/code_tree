n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if a[i] == b[j]:
            dp[i][j] = dp[i+1][j+1] + 1
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j+1])

#print(*dp, sep = '\n')
#####################
target = dp[0][0]
x, y = 0, 0
ans = [0]*target
while True:
    last = float('INF')
    n_x, n_y = 0, 0
    for i in range(x, n):
        for j in range(y, m):
            if dp[i][j] < target:
                break
            if a[i] == b[j] and dp[i][j] == target and a[i] < last:
                last = a[i]
                n_x, n_y = i, j
                ans[target-1] = last
                #print(i, j, ans)
    x, y = n_x, n_y
    target -= 1
    if target <= 0:
        break
ans.reverse()
print(*ans)
