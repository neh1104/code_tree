n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
arr.sort()
a = arr[:n]
b = arr[n:]

m = sys.maxsize

for i in range(n):
    m = min(m, b[i] - a[i])

print(m)