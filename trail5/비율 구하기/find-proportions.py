n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

from sortedcontainers import SortedDict

dt = SortedDict()

for i in words:
    dt[i] = dt.get(i, 0) + 1

for i in dt:
    I = dt[i]/n*100
    print(i, f'{I:.4f}')