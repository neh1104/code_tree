n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

import heapq
pq = []

for x, y in points:
    heapq.heappush(pq, (x+y, x, y))

for _ in range(m):
    xy, x, y = heapq.heappop(pq)
    heapq.heappush(pq, (xy+4, x+2, y+2))

print(*pq[0][1:])