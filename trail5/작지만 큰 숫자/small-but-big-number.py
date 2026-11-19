n, m = map(int, input().split())
sequence = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.

from sortedcontainers import SortedSet
s = SortedSet(sequence)

for q in query:
    idx = s.bisect_right(q)
    if idx:
        print(s.pop(idx-1))
    else:
        print(-1)