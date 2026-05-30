n = int(input())

for i in range(1, 2 * n):
    if i <= n:
        for _ in range(i):
            print('*', end = ' ')
    if i > n:
        for _ in range(2 * n - i):
            print('*', end = ' ')
    print()