n = int(input())

print('* '*n)
for i in range(1, n):
    if i % 2 == 1:
        for _ in range(i):
            print(' ', end = ' ')
        for _ in range(n//2 - (i // 2)):
            print('*', ' ', end = ' ')
        print()
    else:
        for _ in range(i + 1):
            print(' ', end = ' ')
        for _ in range((n//2) - i//2):
            print('*', ' ', end = ' ')
        print()
