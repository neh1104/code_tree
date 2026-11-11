n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

import heapq
pq = []
for a in arr:
    heapq.heappush(pq, -a)

while len(pq) >= 2:
    a = -heapq.heappop(pq)
    b = -heapq.heappop(pq)
    if a != b:
        heapq.heappush(pq, -(a-b))
if pq:
    print(-pq[0])
else:
    print(-1)