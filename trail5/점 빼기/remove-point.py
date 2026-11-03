n, m = map(int, input().split())

# Store points as list of tuples (x, y)
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries
queries = [int(input()) for _ in range(m)]

# Please write your code here.

from sortedcontainers import SortedSet

s = SortedSet(points)


for q in queries:
    l = len(s)
    idx = s.bisect_left((q, 0))
    if idx != l:
        print(*s.pop(idx))
    else:
        print(-1, -1)
    