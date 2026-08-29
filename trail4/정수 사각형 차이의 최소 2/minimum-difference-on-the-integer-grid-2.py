n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

memo = [[[] for _ in range(n)] for _ in range(n)]

memo[0][0] = [(grid[0][0], grid[0][0])]

def add_state(states, new_max, new_min):
    # 새로운 상태가 기존 상태에 지배되는지 확인
    for max_val, min_val in states:
        if max_val <= new_max and min_val >= new_min:
            return

    # 새로운 상태가 기존 상태를 지배한다면 제거
    states[:] = [
        (max_val, min_val)
        for max_val, min_val in states
        if not (new_max <= max_val and new_min >= min_val)
    ]

    states.append((new_max, new_min))


for i in range(n):
    for j in range(n):

        if i == 0 and j == 0:
            continue

        now = grid[i][j]

        # 위에서 오는 경우
        if i > 0:
            for MAX, MIN in memo[i-1][j]:
                new_max = max(MAX, now)
                new_min = min(MIN, now)

                add_state(memo[i][j], new_max, new_min)

        # 왼쪽에서 오는 경우
        if j > 0:
            for MAX, MIN in memo[i][j-1]:
                new_max = max(MAX, now)
                new_min = min(MIN, now)

                add_state(memo[i][j], new_max, new_min)


answer = min(MAX - MIN for MAX, MIN in memo[n-1][n-1])

print(answer)