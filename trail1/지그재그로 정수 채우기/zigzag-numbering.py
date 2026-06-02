n, m = map(int, input().split())

# Please write your code here.

for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            print(i + j*n, end = ' ')
        else:
            print((j+1)*n-i-1, end = ' ')
    print()