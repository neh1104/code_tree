n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
visited = [False] * n
MIN = sys.maxsize

def choose(curr, cost, cnt):
    global MIN

    if cost >= MIN:
        return

    if cnt == n:
        if A[curr][0] != 0:
            MIN = min(MIN, cost + A[curr][0])
        return

    for nxt in range(n):
        if visited[nxt] or A[curr][nxt] == 0:
            continue

        visited[nxt] = True
        choose(nxt, cost + A[curr][nxt], cnt + 1)
        visited[nxt] = False

visited[0] = True
choose(0, 0, 1)

print(MIN)