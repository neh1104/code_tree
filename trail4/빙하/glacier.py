from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = True

time = 0
last = 0

while q:
    next_q = deque()
    melted = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True

            if a[nr][nc] == 1:
                next_q.append((nr, nc))
                melted += 1
            else:
                q.append((nr, nc))

    if not next_q:
        break

    last = melted
    time += 1

    for r, c in next_q:
        a[r][c] = 0

    q = next_q

print(time, last)