n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from sortedcontainers import SortedDict
dt = SortedDict()
line = [0]
for i in range(1, n+1):
    line.append(i)
    dt[i] = [1, set([i])]
for _ in range(3):
    for s, e in edges:
        line[s], line[e] = line[e], line[s]
        if s not in dt[line[s]][1]:
            dt[line[s]][1].add(s)
            dt[line[s]][0] += 1
        if e not in dt[line[e]][1]:
            dt[line[e]][1].add(e)
            dt[line[e]][0] += 1
for d in dt.values():
    print(d[0])