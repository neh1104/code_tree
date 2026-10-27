n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet
s = SortedSet(arr)

for q in queries:
    a = s.bisect_left(q)
    if a == n:
        print(-1)
    else:
        print(s[a])