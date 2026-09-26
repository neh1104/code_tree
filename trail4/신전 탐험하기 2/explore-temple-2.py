n = int(input())
l, m, r = [], [], []

for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.

dp = [[[0]*3 for _ in range(n)] for _ in range(3)]

for t in range(3):
    if t == 0:
        dp[t][0][t] = l[0]
    elif t == 1:
        dp[t][0][t] = m[0]
    else:
        dp[t][0][t] = r[0]

    for i in range(1, n):
        for j in range(3):
            if i == n-1 and j == t:
                continue
            if j == 0:
                s = l[i]
            elif j == 1:
                s = m[i]
            else:
                s = r[i]
            dp[t][i][j] = max(dp[t][i-1][(j+1)%3], dp[t][i-1][(j+2)%3])+s
#print(*dp, sep = '\n')
print(max(max(arr[n-1]) for arr in dp))
