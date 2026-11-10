n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.

import heapq

pq = []

for i in x:
    if i:
        heapq.heappush(pq, -i)
    else:
        if pq:
            print(-heapq.heappop(pq))
        else:
            print(0)