n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

from sortedcontainers import SortedSet
s = SortedSet(i for i in range(1, m+1))
cnt = 0
for i in a:
    idx = s.bisect_right(i)
    if idx == 0:
        break
    s.pop(idx-1)
    cnt += 1
print(cnt)