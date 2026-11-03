n, m = map(int, input().split())

# Store points as list of tuples (x, y)
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries
queries = [int(input()) for _ in range(m)]

# Please write your code here.

from sortedcontainers import SortedSet

s = SortedSet(points)

l = len(s)
for q in queries:
    
    idx = s.bisect_left((q, 0))
    if idx != l:
        print(*s.pop(idx))
        l -= 1
    else:
        print(-1, -1)
    