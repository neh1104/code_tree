# 두 배열의 최장 공통 부분 수열(LCS)을 찾는 프로그램입니다.
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열을 뒤집습니다.
a.reverse()
b.reverse()

a = [0] + a
b = [0] + b

INF = 1987654321

dp = [[0] * (m + 1) for _ in range(n + 1)]
path = [[(0, 0)] * (m + 1) for _ in range(n + 1)]
cur_best = [[INF] * (m + 1) for _ in range(n + 1)]

# 최장 공통 부분 수열을 찾기 위한 동적 프로그래밍을 수행합니다.
# dp[i][j] :: 문자열 a는 i번째까지, 문자열 b는 j번째까지 보았을 때 최장 공통 부분 수열의 길이
# cur_best[i][j] :: 문자열 a는 i번째까지, 문자열 b는 j번째까지 보았을 때 최장 공통 부분 수열 중
# 가장 마지막으로 선택된 값을 최소화시킨 수열의 그 최솟값
# path[i][j] : 그러한 최장 공통 부분 수열이 어느 이전 정보에서 왔는지의 정보
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 각 단계에서 최적의 해를 찾습니다.
        if dp[i - 1][j] > dp[i][j] or (dp[i - 1][j] == dp[i][j] and cur_best[i - 1][j] < cur_best[i][j]):
            dp[i][j] = dp[i - 1][j]
            path[i][j] = (i - 1, j)
            cur_best[i][j] = cur_best[i - 1][j]
        
        if dp[i][j - 1] > dp[i][j] or (dp[i][j - 1] == dp[i][j] and cur_best[i][j - 1] < cur_best[i][j]):
            dp[i][j] = dp[i][j - 1]
            path[i][j] = (i, j - 1)
            cur_best[i][j] = cur_best[i][j - 1]

        if a[i] == b[j] and (dp[i - 1][j - 1] + 1 > dp[i][j] or (dp[i - 1][j - 1] + 1 == dp[i][j] and a[i] < cur_best[i][j])):
            dp[i][j] = dp[i - 1][j - 1] + 1
            path[i][j] = (i - 1, j - 1)
            cur_best[i][j] = a[i]

# 최장 공통 부분 수열을 추적합니다.
lcs = []
i, j = n, m
while i > 0 and j > 0:
    if path[i][j] == (i - 1, j - 1) and a[i] == b[j]:
        lcs.append(a[i])
        i -= 1
        j -= 1
    else:
        i, j = path[i][j]

# 최장 공통 부분 수열을 출력합니다.
print(' '.join(map(str, lcs)))
