n = int(input())

for i in range(1, 2*n):
    for _ in range(abs(n - i)):
        print(' ', end = '')
    for _ in range(n - abs(n-i)):
        print('* ', end = '')
    print()