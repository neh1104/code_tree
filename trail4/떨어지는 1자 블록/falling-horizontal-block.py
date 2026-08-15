n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
k -= 1
I = n-1
for i in range(n):
    for j in range(m):
        if a[i][k+j] == 1:
            I = i-1
            break
    if I != n-1:
        break

for i in range(n):
    for j in range(n):
        if i == I and j in range(k, k+m):
            print(1, end = ' ')
        else:
            print(a[i][j], end = ' ')
    print()