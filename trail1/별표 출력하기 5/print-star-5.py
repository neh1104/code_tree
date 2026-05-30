n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        for k in range(i):
            print('*', end = '')
        print(end = ' ')
    print()