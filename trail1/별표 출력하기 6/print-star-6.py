n = int(input())

for i in range(1, 2*n):
    for _ in range(n - abs(n-i) - 1):
        print(' ', end = ' ')
    for _ in range(abs(2*(n-i)) + 1):
        print('*', end = ' ')
    print()
    