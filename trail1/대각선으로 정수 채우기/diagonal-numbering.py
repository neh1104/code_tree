n, m = map(int, input().split())

# Please write your code here.

a = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num = 1
for i in range(n):
    for j in range(m):
        if a[i][j] != 0:
                #print('ij != 0')
                continue
        for k in range(j+1):
            if i+k >= n:
                #print('i+k>n')
                break
            a[i+k][j-k] = num
            #print(i+k, j-k)
            num += 1

for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()