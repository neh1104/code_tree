n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Please write your code here.

import heapq
arr1.sort()
arr2.sort()

pq = []
# arr1의 각 원소와 arr2[0]의 쌍을 초기 후보로 삽입 (최대 k개까지만 필요)
for i in range(min(n, k)):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

ans = 0
for _ in range(k):
    ans, i, j = heapq.heappop(pq)
    # arr2에 다음 원소가 남아있다면 다음 후보 쌍을 힙에 추가
    if j + 1 < m:
        heapq.heappush(pq, (arr1[i] + arr2[j + 1], i, j + 1))

print(ans)