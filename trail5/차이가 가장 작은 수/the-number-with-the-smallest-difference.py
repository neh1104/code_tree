n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from sortedcontainers import SortedSet
import sys

s = SortedSet(arr)
MIN = sys.maxsize
N = len(s)
for i in range(N):
    find_n = s[i]+m
    idx = s.bisect_left(find_n)
    if idx != N:
        MIN = min(s[idx]-s[i], MIN)

print(MIN if MIN != sys.maxsize else -1)