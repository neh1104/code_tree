n = int(input())

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

a[0][0] = 1
for i in range(1, n):
    a[i][0] = 1
    for j in range(1, i+1):
        a[i][j] = a[i-1][j-1] + a[i-1][j]
        
for i in range(n):
    for j in range(i+1):
        print(a[i][j], end = ' ')
    print()