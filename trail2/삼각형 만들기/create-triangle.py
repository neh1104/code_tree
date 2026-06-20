n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
MAX = 0
m = 10000
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):

                x1 = x[i]+m; y1 = y[i]+m
                x2 = x[j]+m; y2 = y[j]+m
                x3 = x[k]+m; y3 = y[k]+m
                if (x1 == x2 or x2 == x3 or x1 == x3) and (y1== y2 or y2==y3 or y1==y3):
                    S = abs((x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3))
                    MAX = max(MAX, int(S))

print(MAX)