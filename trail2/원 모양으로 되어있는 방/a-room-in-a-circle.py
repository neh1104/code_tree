n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
import sys
MIN = sys.maxsize

for i in range(n):
    p = 0
    sum = 0
    for j in range(n):
        I = (i+j)%n
        sum += a[I]*p
        p += 1

    MIN = min(MIN, sum)

print(MIN)