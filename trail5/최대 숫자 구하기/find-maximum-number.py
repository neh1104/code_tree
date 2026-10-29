n, m = map(int, input().split())
queries = list(map(int, input().split()))

# Please write your code here.

from sortedcontainers import SortedSet

s = SortedSet(i for i in range(1, m+1))

for q in queries:
    s.remove(q)
    print(s[-1])