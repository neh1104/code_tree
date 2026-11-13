n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.

import heapq
pq = []

for i in x:
    if i == 0:
        if pq:
            print(pq[0][0]*pq[0][1])
            heapq.heappop(pq)
        else:
            print(0)
    else:
        heapq.heappush(pq, (abs(i), 1 if i > 0 else -1))
