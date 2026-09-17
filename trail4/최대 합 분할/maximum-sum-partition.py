n = int(input())
arr = list(map(int, input().split()))

S = sum(arr)
NEG = -1

dp = [NEG] * (2 * S + 1)
dp[S] = 0

for x in arr:
    ndp = dp.copy()

    for d in range(-S, S + 1):
        cur = dp[d + S]

        if cur == NEG:
            continue

        ndp[d + x + S] = max(
            ndp[d + x + S],
            cur + x
        )

        ndp[d - x + S] = max(
            ndp[d - x + S],
            cur + x
        )

    dp = ndp

print(dp[S] // 2)