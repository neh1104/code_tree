n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
E, T = 0, 0
for e, t in quests:
    E += e
    T += t

l = E-m
if l < 0:
    print(-1)
else:
    dp = [-1]*(l+1)
    dp[0] = 0
    for e, t in quests:
        for i in range(l, e-1, -1):
            idx = i-e
            if dp[idx] != -1:
                dp[i] = max(dp[i], dp[idx]+t)

    print(T-max(dp))