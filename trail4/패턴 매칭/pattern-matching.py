import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

n, m = len(s), len(p)

# dp[i][j]: s[:i]와 p[:j]가 매칭되는지 여부
dp = [[False] * (m + 1) for _ in range(n + 1)]

# 빈 문자열과 빈 패턴은 매칭됨
dp[0][0] = True

# 빈 문자열 s에 대해, 'a*' 처럼 0개 매칭으로 넘어갈 수 있는 패턴 처리
for j in range(2, m + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]

# DP 테이블 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            # 1. '*'를 0개 사용 (앞 문자 + '*' 패턴 2개 건너뜀)
            dp[i][j] = dp[i][j - 2]
            
            # 2. '*'를 1개 이상 사용 (앞 문자가 현재 s 문자와 일치할 때)
            prev_char = p[j - 2]
            if prev_char == '.' or prev_char == s[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
        else:
            # 단일 문자 또는 '.' 매칭
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

if dp[n][m]:
    print("true")
else:
    print("false")