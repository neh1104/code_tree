n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
MIN = 40000*40000
for i in range(n):
    X = []; Y = []
    for j in range(n):
        if i == j:
            continue
        X.append(x[j])
        Y.append(y[j])
    ln_x = max(X)-min(X)
    ln_y = max(Y)-min(Y)
    MIN = min(MIN, ln_x*ln_y)

print(MIN)