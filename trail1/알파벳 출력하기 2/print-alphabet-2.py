n = int(input())
ch = ord('A')

for i in range(n):
    for _ in range(i):
        print(' ', end = ' ')
    for j in range(n-i):
        print(chr(ch), end = ' ')
        ch+=1
        if chr(ch-1) == 'Z':
            ch = ord('A')
    print()