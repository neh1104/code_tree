n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

import heapq
pq = []
j = 1
for i in arr:
    heapq.heappush(pq, i)
    if j <= 2:
        print(-1)
        j += 1
    else:
        a, b, c = (heapq.heappop(pq) for i in range(3))
        print(a*b*c)
        heapq.heappush(pq, c)
        heapq.heappush(pq, b)
        heapq.heappush(pq, a)