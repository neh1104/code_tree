n = int(input())

for i in range(2*n + 1):
    if i % 2 == 0:
        for _ in range(2*n + 1):
            print('*', end = ' ')
    else:
        for _ in range(n + 1):
            for __ in range(1):
                print('*', end = ' ')
                print(' ', end = ' ')
    print()