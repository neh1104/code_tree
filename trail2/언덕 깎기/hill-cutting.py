N = int(input())
h = [int(input()) for _ in range(N)]

# Please write your code here.
import sys
MAX = sys.maxsize
for i in range(min(h), max(h)+1):
    x = [0, 0]
    for n in range(N):
        if h[n]- i > 8:
            x[0] += (h[n]-i-8)**2
        elif i - h[n] > 9:
            x[0] += (i-h[n]-9)**2
        if h[n] - i > 9:
            x[1] += (h[n]-i-9)**2
        elif i - h[n] > 8:
            x[1] += (i-h[n]-8)**2
    x = min(x)
    MAX = min(MAX, x)

print(MAX)