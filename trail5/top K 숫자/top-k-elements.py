n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

from sortedcontainers import SortedSet

s = SortedSet(arr)
n = len(s)
for i in range(k):
    print(s[n-i-1], end = ' ')