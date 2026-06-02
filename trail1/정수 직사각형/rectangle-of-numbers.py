n, m = map(int, input().split())

a = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num = 1
for i in range(n):
    for j in range(m):
        a[i][j] = num
        num += 1

for i in a:
    for j in i:
        print(j, end = ' ')
    print()