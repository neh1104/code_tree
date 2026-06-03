n = int(input())

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
low = 0
for i in range(n-1,-1, -1):
    for j in range(n-1,-1, -1):
        if low % 2 == 0:
            a[j][i] = cnt 
        else:
            a[n-j-1][i] = cnt
        cnt += 1
    low += 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()