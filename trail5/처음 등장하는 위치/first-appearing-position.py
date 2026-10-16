n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

from sortedcontainers import SortedDict

dt = SortedDict()
idx = 1
for i in arr:
    dt[i] = dt.get(i, idx)
    idx += 1

for i in dt:
    print(i, dt[i])