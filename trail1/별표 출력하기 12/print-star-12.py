n = int(input())
print('* '*n)
for i in range(n-1):
    for j in range(n):
        if i>=j:
            print(' ', end = ' ')
            continue
        if j % 2 == 1:
            print('*', end = ' ')
            continue
        else:
            print(' ', end = ' ')
            continue
    print()