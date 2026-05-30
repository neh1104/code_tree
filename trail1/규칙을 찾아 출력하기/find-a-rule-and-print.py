n = int(input())

print('* '*n)
for i in range(n-1):
    for j in range(n):
        if j == 0 or j == n-1:
            print('*', end = ' ')
        elif i >= j:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()
        