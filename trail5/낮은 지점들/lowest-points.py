n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
INT_MAX = sys.maxsize

dt = dict()
for x, y in points:
    dt[x] = min(y, dt.get(x, INT_MAX))

print(sum(dt.values()))