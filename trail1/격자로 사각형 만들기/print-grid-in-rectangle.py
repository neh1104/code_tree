n = int(input())

a = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i-1][j] + a[i][j-1]\
                  + a[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()