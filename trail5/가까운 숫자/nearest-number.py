n = int(input())
queries = list(map(int, input().split()))

# Please write your code here.

from sortedcontainers import SortedSet
import sys

length = sys.maxsize
s = SortedSet([0])
for q in queries:
    s.add(q)
    now = s.bisect_left(q)

    if now == len(s)-1:
        length = min(q-s[now-1], length)
    elif now == 0:
        length = min(s[now+1]-q, length)
    else:
        length = min(s[now+1]-q, q-s[now-1], length)
    print(length)