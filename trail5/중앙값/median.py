t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    # Please write your code here.
    import heapq
    pq = []
    set_ls = []
    for i in range(m):
        heapq.heappush(pq, arr[i])
        if i % 2 == 0:
            now_pop = heapq.heappop(pq)
            heapq.heappush(set_ls, -now_pop)

            if now_pop == -set_ls[0]:
                print(now_pop, end = ' ')
            else:
                while True:
                    heapq.heappush(pq, -heapq.heappop(set_ls))
                    heapq.heappush(set_ls, -heapq.heappop(pq))
                    if -set_ls[0] <= pq[0]:
                        break
                print(-set_ls[0], end = ' ')      
    print()