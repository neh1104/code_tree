n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

MIN = 1000000*2

for i in range(n-1):
    for j in range(i+1, n):
        ln = (x[i]-x[j])**2 + (y[i]-y[j])**2

        MIN = min(MIN, ln)

print(MIN)