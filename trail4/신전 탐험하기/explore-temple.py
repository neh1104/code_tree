n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.

dp = [[0]*3 for _ in range(n)]
dp[0] = [l[0], m[0], r[0]]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            s = l[i]
        elif j == 1:
            s = m[i]
        else:
            s = r[i]

        dp[i][j] = max(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])+s
#print(*dp, sep= '\n')
print(max(dp[n-1]))