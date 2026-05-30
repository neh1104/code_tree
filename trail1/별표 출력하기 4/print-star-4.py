n = int(input())

for i in range(2*n -1):
    if i < n:
        for _ in range(n - i):
            print('*', end = ' ')
    else:
        for _ in range(i-(n-2)):
            print('*', end = ' ')
    print()