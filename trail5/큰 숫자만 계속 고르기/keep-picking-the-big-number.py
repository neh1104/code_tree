n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

import heapq

pq = [-i for i in arr]
heapq.heapify(pq)

for _ in range(m):
    a = heapq.heappop(pq)
    heapq.heappush(pq, a+1)
print(-pq[0])