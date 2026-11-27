N = int(input())
a, t = [], []
for _ in range(N):
    ai, ti = map(int, input().split())
    a.append(ai)
    t.append(ti)

# Please write your code here.
import heapq

pq = []
for i in range(N):
    heapq.heappush(pq, (a[i], i+1, t[i]))
A, B, C = heapq.heappop(pq)
tmp = [(B, A, C)]
time = 0; MAXWAIT = 0
while True:
    if not tmp:
        if not pq:
            break
        else:
            A, B, C = heapq.heappop(pq)
            heapq.heappush(tmp, (B, A, C))

    _, ps, pt = heapq.heappop(tmp)
    WAIT = time - ps if ps < time else 0
    MAXWAIT = max(MAXWAIT, WAIT)
    time = ps+pt if time <= ps else time+pt
    #print(_, MAXWAIT)

    while True:
        if not pq or pq[0][0] > time :
            break
        A, B, C = heapq.heappop(pq)
        heapq.heappush(tmp, (B, A, C))
print(MAXWAIT)