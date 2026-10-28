n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

from sortedcontainers import SortedSet

s = SortedSet(points)

for x, y in queries:
    i = s.bisect_right((x, y))
    if i == n:
        print(-1, -1)
    else:
        print(s[i][0], s[i][1])