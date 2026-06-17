n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys

def dis(x, x2):
    return abs(x-x2)

MIN = sys.maxsize

for i in range(1, n-1):
    n_x = x[:i]+x[i+1:]
    n_y = y[:i]+y[i+1:]

    sum = 0
    for j in range(n-2):
        dif_x = dis(n_x[j], n_x[j+1])
        dif_y = dis(n_y[j], n_y[j+1])
        sum += dif_x + dif_y
        
    MIN = min(MIN, sum)

print(MIN)