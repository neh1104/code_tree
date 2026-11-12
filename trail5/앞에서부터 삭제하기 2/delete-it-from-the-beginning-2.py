import sys
import heapq

input = sys.stdin.read
def solve():
    data = input().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:]]
    
    pq = []
    for i, x in enumerate(arr):
        heapq.heappush(pq, (x, i))
    
    SUM = sum(arr)
    MAX = 0
    
    for k in range(1, n - 1):
        SUM -= arr[k - 1]
        
        while pq and pq[0][1] < k:
            heapq.heappop(pq)
            
        s = SUM - pq[0][0]
        avg = s / (n - k - 1)
        MAX = max(MAX, avg)
        
    print(f"{MAX:.2f}")

solve()